# WebScraper-2(c-128)
# @SauhardoSengupta
from selenium import webdriver
import csv
import time
from bs4 import BeautifulSoup
import pandas as pd

# The url from where we will scrape the data....
URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

# Creating the browser to open the url in Chrome
browser = webdriver.Chrome("C:/Users/sengu/Downloads/chromedriver")
browser.get(URL)

# Letting the webpage load by letting the programme sleep for 10seconds
time.sleep(10)

# Creating a function to Scrape the data from the website


def WebScraper():
    Headers = ["Stars", "Constellation", "Right ascension", "Declination"]

    Planet_Data = []

    for i in range(0, 428):
        soup = BeautifulSoup(browser.page_source, "html.parser")

        Table = soup.find(
            "table",attrs={"class", "wikitable sortable jquery-tablesorter"})

        temp_list = []
        table_rows = Table.find_all("tr")

        for tr in table_rows:
            td = tr.find_all("td")
            row = [i.text.rstrip() for i in td]
            temp_list.append(row)

        Star_Name = []
        Distance = []
        Mass = []
        Radius = []

        for i in range(1, len(temp_list)):
            Star_Name.append(temp_list[i][0])
            Distance.append(temp_list[i][5])
            Mass.append(temp_list[i][7])
            Radius.append(temp_list[i][8])

        df2 = pd.DataFrame(list(zip(Star_Name, Distance, Mass, Radius)),columns=Headers)

        df2.to_csv()

WebScraper()
