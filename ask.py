import requests
from enum import Enum
import typer
from pprint import pprint
import webbrowser
from youtubesearchpython import VideosSearch

main = typer.Typer()
headers = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}

@main.command()
@main.command("w")
def wikipedia(query: str):
    query = f"{query}"
    search_url="https://en.wikipedia.org/w/api.php"
    params={
        "action":"query",
        "format":"json",
        "generator":"prefixsearch",
        "prop":"pageprops|description|info",
        "inprop":"url",
        "gpslimit":"1",
        "gpssearch":query
        }
    r = requests.get(search_url, params=params, headers=headers)
    try:
        j = r.json()
        url = list(j['query']['pages'].values())[0]['fullurl']
        webbrowser.open(url)
    except Exception as e:
        print(e)
        print("No results found!")

@main.command()
@main.command("y")
def youtube(query: str):
    query = f"{query}"
    r = VideosSearch(query, limit = 1)
    try:
        r = r.result()
        url = r['result'][0]['link']
        webbrowser.open(url)
    except Exception as e:
        print(e)
        print("No results found!")

if __name__ == '__main__':
    main()
