import json
import requests
import pandas as pd
from configs import passwords

subscription_key = passwords.api_key
endpoint = passwords.api_endpoint
search_url = "https://api.bing.microsoft.com/v7.0/news/search"

# Query term(s) to search for. 
query = "HSV"

# Construct a request
mkt = 'de-DE'
count = 1000
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
        result_list.append(article["description"])
except Exception as ex:
    raise ex

with open("result8.json", "w") as file:
    json.dump(result_list, file)

search_list = ["HSV", "Hamburger Sport Verein"]

