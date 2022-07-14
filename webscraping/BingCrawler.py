import json
import requests
import pandas as pd

from configs import passwords

# Add your Bing Search V7 subscription key and endpoint to your environment variables.
subscription_key = passwords.api_key
endpoint = passwords.api_endpoint
search_url = "https://api.bing.microsoft.com/v7.0/news/search"

# Query term(s) to search for. 
query = "HSV"

# Construct a request
mkt = 'de-DE'
count = 99
params = { 'q': query, 'mkt': mkt, 'count': count, 'textDecorations': True, 'textFormat': "HTML"}
headers = { 'Ocp-Apim-Subscription-Key': subscription_key }


result_list = []

# Call the API
print("test")
try:
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_result = response.json()

    for article in search_result['value']:
        #print(article["description"])
        result_list.append(article["description"])
    # description = [article["description"] for article  in search_result['value']]
    # print(description)

except Exception as ex:
    raise ex

x = result_list[0]

print(result_list[0])

def check_for_words(search):
    for item in result_list:
        for word in search:
            if word in item:
                print(word)

search_list = ["HSV", "Hamburger"]

check_for_words(search_list)

