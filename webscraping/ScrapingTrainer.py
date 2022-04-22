from bs4 import BeautifulSoup
import requests

#request try

url = "https://www.weltfussball.de/teams/hamburger-sv/9/"

resp = requests.get(url)

soup =  BeautifulSoup(resp.content)


x = soup.select_one('#site > div.white > div.content > div > div:nth-child(2) > div')

t_list = []

for i in x:
    t_list.append(i.get_text())

t_list = [t.split("\n") for t in t_list]

t_list.pop(0)
t_list.pop(1)

t_list = [tr for t in t_list for tr in t]

res = list(filter(None, t_list))
res = res[4:]

chunks = [res[i:i+2] for i in range(0, len(res), 3)]

print(chunks)