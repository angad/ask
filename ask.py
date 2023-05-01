""" ask.py - I am feeling lucky search """

import jq
import requests
import typer
import webbrowser
import yaml
from flask import Flask, request, send_from_directory

search_params = yaml.load(open("search_params.yml"), Loader=yaml.FullLoader)

main = typer.Typer()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

app = Flask(__name__)
cors_headers = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET",
    "Access-Control-Allow-Headers": "Content-Type, openai-ephemeral-user-id, openai-conversation-id",
    "Access-Control-Max-Age": "3600",
}

SOURCE = "search"
QUERY = "content"


@main.command()
def search(source: str, query: str) -> None:
    url = execute(source, query)
    url_handler(url, open_browser=True)


@app.route("/", methods=["GET", "OPTIONS"])
def api():
    source = request.args.get(SOURCE)
    query = request.args.get(QUERY)
    if request.method == "OPTIONS":
        return ("", 204, cors_headers)
    if not (source and query):
        return ("", 400, cors_headers)
    result = execute(request.args.get(SOURCE), request.args.get(QUERY))
    if result:
        return ({"url": result}, 200, cors_headers)
    else:
        return ({}, 404, cors_headers)


@app.route("/openapi.yaml", methods=["GET", "OPTIONS"])
def openapi():
    host = request.headers.get("Host")
    if request.method == "OPTIONS":
        return ("", 204, cors_headers)
    with open("openapi.yaml") as f:
        manifest = f.read().replace("{{host}}", host)
        return (manifest, 200, cors_headers)


@app.route("/.well-known/ai-plugin.json", methods=["GET", "OPTIONS"])
def ai_plugin():
    host = request.headers.get("Host")
    if request.method == "OPTIONS":
        return ("", 204, cors_headers)
    with open("manifest.json") as f:
        manifest = f.read().replace("{{host}}", host)
        return (manifest, 200, cors_headers)


@app.route("/logo.png", methods=["GET", "OPTIONS"])
def logo():
    if request.method == "OPTIONS":
        return ("", 204, cors_headers)
    return send_from_directory(".", "logo.png", mimetype="image/png")


def execute(source: str, query: str) -> str:
    if len(source) == 1:
        site_source = search_params[get_site(search_params, source)]
    else:
        site_source = search_params[source]
    params = search_and_replace(site_source["params"], "$query", f"{query}")
    try:
        if "url" in site_source:
            response = requests.get(
                site_source["url"], params=params, headers=headers
            ).json()
        if "func" in site_source:
            module = __import__(site_source["module"])
            func = getattr(module, site_source["func"])
            response = func(query, **params).result()
        url = jq.compile(site_source["response_parser"]).input(response).first()
        if "response_append" in site_source:
            url = site_source["response_append"] + url
        return url
    except Exception as exception:
        print(exception)
        print("No results found!")
        return None


def url_handler(url: str, open_browser: bool = False) -> None:
    if url:
        print(url)
        if open_browser:
            webbrowser.open(url)
    else:
        print("No URL!")


def search_and_replace(
    search_dict: dict, search_value: str, replace_value: str
) -> dict:
    """function to search and replace a value in dictionary"""
    for key, value in search_dict.items():
        if value == search_value:
            search_dict[key] = replace_value
    return search_dict


def get_site(params, short):
    """function to return key for a value in dictionary"""
    for key, value in params.items():
        if isinstance(value, dict):
            for k, v in value.items():
                if k == "short" and v == short:
                    return key


if __name__ == "__main__":
    main()
