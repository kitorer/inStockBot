import json
import smtplib
from time import sleep
from datetime import datetime
from email.message import EmailMessage
from zoneinfo import available_timezones
import mouse
import bs4

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# yeah this probably relies on cookies working
url = "https://www.bestbuy.com/site/searchpage.jsp?id=pcat17071&qp=soldout_facet%3DAvailability~Exclude%20Out%20of%20Stock%20Items%5Estorepickupstores_facet%3DStore%20Availability%20-%20In%20Store%20Pickup~571&st=graphics+card"

# debug lines
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True) 

s = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service = s) 
# debug
# driver = webdriver.Chrome(options=options)

log = ""

# using best buy search bar
# returns a boolean
def searchbar(item_to_search):
    try:
        searchbar = driver.find_element(By.ID, "gh-search-input")
        searchbar.send_keys(item_to_search)
        searchbar.send_keys(Keys.RETURN)

        return True
    except:
        return False

# has to be on the searched page 
# ToDo: get it print where which item is available
# the fulfillment comments were attempts for location tagging
def isAvailable():
    html = driver.page_source
    soup = bs4.BeautifulSoup(html,"html.parser")

    items = soup.find_all("li", {"class": "sku-item"})

    for product in items:
        hrefs = product.find(href = True)
        #fulfillmentID = product.find(By.ID,"fulfillment-fulfillment-summary")
        #fulfillmentText = fulfillmentID.find("strong")
        link = "https://www.bestbuy.com" + hrefs['href']
        return link

        #print(fulfillmentID['strong'])
        
# ping every 5 minutes or something
# call notify if there is a new item that passes in the new items
def checker():
    linkStorage = []
    print()

def notify():
    print()

def main():
    driver.get(url)
    print(driver.title)
    sleep(2)
    isAvailable()
    driver.close()

if __name__ == "__main__":
    main()
