# Ask - I am feeling lucky for popular sites on command line

Goal: Search popular websites from your command line. Returns first result URL
based on keyword search. Currently only Wikipedia is implemented.

Might migrate to Python if things get tough with Bash.

## Usage

    $ ./ask.sh elon musk
    https://en.wikipedia.org/?curid=909036

## Dependencies

curl, jq

## TODO

- More sites
  - YouTube
  - Reddit
  - DuckDuckGo
- Result picker
