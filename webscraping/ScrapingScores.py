from datetime import datetime
from operator import ne
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd



f = "football-data/clean.csv"


#chromedriver location
# path = r"C:\Users\maxbl\Downloads\chromedriver_win32\chromedriver.exe"

# #target of the document
# url = "https://www.football-data.co.uk/germanym.php"
# element = "/html/body/table[5]/tbody/tr[2]/td[3]/a[3]"

#selenium try
def scraping(path, url, element):

    options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": "/Users/max/Desktop/OpenData-HSV-Study/webscraping"}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(path, chrome_options = options)

    driver.get(url)
    time.sleep(2)
    driver.find_element_by_xpath(element).click()

    time.sleep(5)
    driver.quit()

#scraping(url)

old_path = "football-data/clean.csv"
new_path = "football-data/test.csv"
update_path = "football-data/update.csv"

with open(old_path, 'r') as t1, open(new_path, 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

with open(update_path, 'w') as outFile:
    for line in filetwo:
        if line not in fileone:
            outFile.write(line)
