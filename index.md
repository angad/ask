# Ask
### I am feeling lucky for popular sites on command line

Search popular websites from your command line quickly.

![](https://github.com/angad/ask/blob/gh-pages/output.gif?raw=true)

## Supported sites

- DuckDuckGo (`d`)
- Github (`g`)
- Reddit (`r`)
- Twitter (`t`)
- Wikipedia (`w`)
- Youtube (`y`)

## TODO sites

- Twitter

## Usage

Generate the Python Executable (.pex) file

    $ ./build.sh

Run `ask.pex` file with search site and search query

    $ ./ask.pex w 'elon musk'
    https://en.wikipedia.org/?curid=909036

Alternatively, you can just install the requirements and run the python file

    $ pip3 install -r requirements.txt
    $ python3 ask.py w 'elon musk'

## Dependencies

    typer # commandline utilities
    requests # HTTP requests library
    youtube-search-python # makes searching youtube easier
    pex # packaging to pex file

## TODO features
- Result picker
- Advanced Search - Search params
