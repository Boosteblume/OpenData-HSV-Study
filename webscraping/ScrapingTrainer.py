import urllib
from bs4 import BeautifulSoup
import requests


#request try

url = "https://www.weltfussball.de/teams/hamburger-sv/9/"

html_content = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html_content)

print(soup.prettify())