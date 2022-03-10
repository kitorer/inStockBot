import json
import smtplib
from time import sleep
from datetime import datetime
from email.message import EmailMessage
import mouse

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://www.bestbuy.com"
#debug lines
#options = webdriver.ChromeOptions()
#options.add_experimental_option("detach", True) 

s = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service = s) 
#debug
#driver = webdriver.Chrome(options=options)

log = ""
# Boolean: returns true if word is found in the url
def isInStock(url, word):
    print("hellow")

#using best buy search bar
#returns a boolean
def searchbar(item_to_search):
    try:
        searchbar = driver.find_element(By.ID, "gh-search-input")
        searchbar.send_keys(item_to_search)
        searchbar.send_keys(Keys.RETURN)

        return True
    except:
        return False

def searchFilters():
    driver.find_element(By.ID, "store-pickup-pickuptoday").click
    sleep(2)
    driver.find_element(By.ID, "soldout_facet-Exclude-Out-of-Stock-Items-0").click
    sleep(2)

    print("this worked")

def main():
    driver.get(url)

    #dont miss out on the latest deals and more
    sleep(5)
    print("5s has passed")
    mouse.click()

    sleep(3)
    print("3s has passed")
    searchbar("graphics cards")

    sleep(3)
    searchFilters()

    print(driver.title)

if __name__ == "__main__":
    main()
