import time
from selenium import webdriver
import pandas as pd

url = r"https://www.wunderground.com/history/daily/EDDH/date/2010-9-25"
f = "football-data/clean.csv"

date_list = []

def dates():
    df = pd.read_csv(f)

    ham_all = df.loc[(df['HomeTeam'] == "Hamburg") | (df['AwayTeam'] == "Hamburg")]
    ham_all.fillna(0, inplace = True)

    new_df = ham_all[ham_all.columns[0:22]]

    global date_list
    date_list = new_df['Date'].to_list()

dates()

def scraping ():
    path = r"C:\Users\maxbl\Downloads\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get(url)
    time.sleep(4)
    driver.quit()

scraping()
