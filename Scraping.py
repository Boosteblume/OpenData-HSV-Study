from dataclasses import dataclass
from datetime import datetime
from re import U
import time
from selenium import webdriver
import pandas as pd
import requests
from bs4 import BeautifulSoup

f = "football-data/clean.csv"

date_list = []

def dates():
    df = pd.read_csv(f)

    ham_all = df.loc[(df['HomeTeam'] == "Hamburg") | (df['AwayTeam'] == "Hamburg")]
    ham_all.fillna(0, inplace = True)

    new_df = ham_all[ham_all.columns[0:22]]

    global date_list
    date_list = new_df['Date'].to_list()

    date_list = [datetime.strptime(date, "%d/%m/%Y") for date in date_list]
    date_list = [date.strftime("%Y-%m-%d") for date in date_list]

#dates()


weather ="https://www.weatherapi.com/docs/"
#request try

req_html = requests.get(url)
html_content = req_html.content
soup = BeautifulSoup(html_content, 'html.parser')
text = soup.find_all(text = True)
print(text)

#selenium try
# def scraping (url):
#     path = r"C:\Users\maxbl\Downloads\chromedriver_win32\chromedriver.exe"
#     driver = webdriver.Chrome(path)
#     driver.get(url)
#     time.sleep(4)


# for i in date_list:
#     url = f"https://www.wunderground.com/history/daily/EDDH/date/{i}"
#     scraping(url)