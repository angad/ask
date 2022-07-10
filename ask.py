""" ask.py - I am feeling lucky search """

import webbrowser
import requests
import typer
from youtubesearchpython import VideosSearch

main = typer.Typer()
headers = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}

@main.command()
@main.command("w")
def wikipedia(query: str):
    ''' Search wikipedia '''
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
    response = requests.get(search_url, params=params, headers=headers)
    try:
        json_response = response.json()
        url = list(json_response['query']['pages'].values())[0]['fullurl']
        webbrowser.open(url)
    except Exception as exception:
        print(exception)
        print("No results found!")

@main.command()
@main.command("y")
def youtube(query: str):
    ''' Search youtube '''
    query = f"{query}"
    response = VideosSearch(query, limit = 1)
    try:
        json_response = response.result()
        url = json_response['result'][0]['link']
        webbrowser.open(url)
    except Exception as exception:
        print(exception)
        print("No results found!")

@main.command()
@main.command("r")
def reddit(query: str):
    ''' Search reddit '''
    query = f"{query}"
    search_url="https://www.reddit.com/search.json"
    params = {
        "q":query,
        "sort":"hot",
        "limit":1
    }
    response = requests.get(search_url, params)
    try:
        json_response= response.json()
        if 'error' in json_response and json_response['error'] == 429:
            raise ValueError("Reddit wants you to slow down and try after sometime!")
        url = "https://reddit.com" + json_response["data"]["children"][0]["data"]["permalink"]
        webbrowser.open(url)
    except Exception as exception:
        print(exception)
        print("No results found!")


@main.command()
@main.command("g")
def github(query: str):
    ''' Search github '''
    query = f"{query}"
    search_url = "https://api.github.com/search/repositories"
    params = {
            "q": query,
            "sort": "stars",
            "per_page": 1
            }
    response = requests.get(search_url, params, headers=headers)
    try:
        json_response = response.json()
        url = json_response['items'][0]['html_url']
        webbrowser.open(url)
    except Exception as exception:
        print(exception)
        print("No results available!")



if __name__ == '__main__':
    main()
