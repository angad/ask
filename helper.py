import webbrowser

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

def url_handler(url: str):
    if url:
        print(url)
        webbrowser.open(url)
    else:
        print("No URL!")
    
# function to search and replace a value in dictionary
def search_and_replace(search_dict, search_value, replace_value):
    for key, value in search_dict.items():
        if value == search_value:
            search_dict[key] = replace_value
    return search_dict

# function to return key for a value in dictionary
def get_site(params, short):
    for key, value in params.items():
        if isinstance(value, dict):
            for k, v in value.items():
                if k == 'short' and v == short:
                    return key 