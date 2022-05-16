#!/bin/bash
#set -ex

query=$@
search_url="https://en.wikipedia.org/w/api.php"
params=(
    "action=query"
    "format=json"
    "generator=prefixsearch"
    "prop=pageprops|description|info"
    "redirects="
    "ppprop=displaytitle"
    "inprop=url"
    "gpsnamespace=0"
    "gpslimit=6"
)

urlencode="--data-urlencode "
curl_params=""
for param in "${params[@]}"; do
    curl_params+="${urlencode} $param "
done

result=`curl -s $curl_params $urlencode "gpssearch=$query" $search_url \
    | jq '.query.pages | map(select(.index == 1)) | .[0].fullurl' 2>/dev/null`

if [ -z "$result" ]
then
    echo "No results found!"
else
    echo $result
fi
