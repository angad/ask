# Ask
### I am feeling lucky for popular sites on command line

Search popular websites from your command line quickly.

## Supported sites

- Youtube (`y`)
- Wikipedia (`w`)
- Reddit (`r`)
- Github (`g`)

## TODO sites

- DuckDuckGo

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

    typer # for commandline utilities
    youtube-search-python # makes searching youtube easier
    pex # packaging to pex file

## TODO features
- Result picker
- Advanced Search - Search params
