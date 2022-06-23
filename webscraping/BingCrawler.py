import json
import requests
from IPython.display import HTML

from configs import passwords

'''
This sample makes a call to the Bing Web Search API with a query and returns relevant web search.
Documentation: https://docs.microsoft.com/en-us/bing/search-apis/bing-web-search/overview
'''

# Add your Bing Search V7 subscription key and endpoint to your environment variables.
subscription_key = passwords.api_key
endpoint = passwords.api_endpoint
search_url = "https://api.bing.microsoft.com/v7.0/news/search"

# Query term(s) to search for. 
query = "HSV"

# Construct a request
mkt = 'de-DE'
params = { 'q': query, 'mkt': mkt , 'textDecorations': True, 'textFormat': "HTML"}
headers = { 'Ocp-Apim-Subscription-Key': subscription_key }

#curl -H "Ocp-Apim-Subscription-Key: <yourkeygoeshere>" https://api.bing.microsoft.com/v7.0/news/trendingtopics
# Call the API
print("test")
try:
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = json.dumps(response.json())
    #descriptions = [article["description"] for article in search_results["value"]]

    print(search_results)

    print("nope")

except Exception as ex:
    print("Fuck!")
    raise ex