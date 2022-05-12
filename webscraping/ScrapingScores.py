from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd


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

#chromedriver location
path = r"C:\Users\maxbl\Downloads\chromedriver_win32\chromedriver.exe"

#target of the document
url = "https://www.football-data.co.uk/germanym.php"
element = "/html/body/table[5]/tbody/tr[2]/td[3]/a[3]"

#selenium try
def scraping (path, url, element):

    options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": "/Users/max/Desktop/OpenData-HSV-Study/webscraping"}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(path, chrome_options = options)

    driver.get(url)
    time.sleep(2)
    driver.find_element_by_xpath(element).click()

    time.sleep(5)
    driver.quit()

scraping(url)

