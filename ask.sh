#!/bin/bash
#set -ex

query=$@
search_url="https://en.wikipedia.org/w/api.php"
params=(
    "action=query"
    "format=json"
    "generator=prefixsearch"
    "prop=pageprops|description"
    "redirects="
    "ppprop=displaytitle"
    "gpsnamespace=0"
    "gpslimit=6"
)

urlencode="--data-urlencode "
curl="curl --get "
curl_params=""
for param in "${params[@]}"; do
    curl_params+="${urlencode} $param "
done

pageid=`curl -s $curl_params $urlencode "gpssearch=$query" $search_url \
    | jq '.query.pages | map(select(.index == 1)) | .[0].pageid' 2>/dev/null`

page_url="https://en.wikipedia.org/?curid="

if [ -z "$pageid" ]
then
    echo "No results found!"
else
    echo $page_url$pageid
fi
