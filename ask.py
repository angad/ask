""" ask.py - I am feeling lucky search """

import jq
import requests
import typer
import yaml

from helper import *

main = typer.Typer()
search_params = yaml.load(open('search_params.yml'), Loader=yaml.FullLoader)

@main.command()
def search(source, query):
    site_source = search_params[get_site(search_params, source)]
    params = search_and_replace(site_source['params'], "$query", f"{query}")
    response = []
    try:
        if "url" in site_source:
            response = requests.get(site_source['url'], params=params, headers=headers).json()
        if "func" in site_source:
            module = __import__(site_source['module'])
            func = getattr(module, site_source['func'])
            response = func(query, **params).result()
        url = jq.compile(site_source['response_parser']).input(response).first()
        if "response_append" in site_source:
            url = site_source["response_append"] + url
        url_handler(url)
    except Exception as exception:
        print(exception)
        print("No results found!")

if __name__ == '__main__':
    main()