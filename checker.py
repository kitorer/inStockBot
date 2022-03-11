import smtplib
from time import sleep
from datetime import datetime
from email.message import EmailMessage
from zoneinfo import available_timezones
import requests
import json

import bs4
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from telegram import Chat

# yeah this probably relies on cookies working
url = "https://www.bestbuy.com/site/searchpage.jsp?id=pcat17071&qp=soldout_facet%3DAvailability~Exclude%20Out%20of%20Stock%20Items%5Estorepickupstores_facet%3DStore%20Availability%20-%20In%20Store%20Pickup~571&st=graphics+card"
API_KEY = ''
s = Service("C:\Program Files (x86)\chromedriver.exe")
Chat_ids = []

driver = webdriver.Chrome(service = s) 

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

# @returns a list of products links fetched from the item list
# has to be on the searched page 
# ToDo: get it print where which item is available
# the fulfillment comments were attempts for location tagging
def isAvailable():
    link_list = []
    html = driver.page_source
    soup = bs4.BeautifulSoup(html,"html.parser")

    items = soup.find_all("li", {"class": "sku-item"})

    for product in items:
        hrefs = product.find(href = True)
        #fulfillmentID = product.find(By.ID,"fulfillment-fulfillment-summary")
        #fulfillmentText = fulfillmentID.find("strong")
        link = "https://www.bestbuy.com" + hrefs['href']
        link_list.append(link)
        print("line 54")

    return link_list
        
# ping every 5 minutes or something
# call notify if there is a new item that passes in the new items
def check():
    #keeps track of items in stock
    #items need to be removed if they do not show up in link_list
    linkStorage = []

    #check for new users
    #telegram()

    link_list = isAvailable()
    print("line 73")
    for items in link_list:
        if(items not in linkStorage):
            notify(True,items)
            linkStorage.append(items)
            print(items)
            print("line 79")
        
    for items in linkStorage:
        if(items not in link_list):
            notify(False,items)
            linkStorage.remove(items)
            print("removed")

#True = in stock
#False = out of stock
def notify(status, link):

    if(status == True):
        message = "In Stock\n" + link

        #for chats in Chat_ids:
        #    sendmsg(message, chats)
        requests.get("https://api.telegram.org/bot<apikey>/sendMessage?chat_id=293457643&text=" + message)
    else:
        message = "Out of Stock\n" + link
        for chats in Chat_ids:
            sendmsg(message, chats)    


def telegramBot(message):
    print()

def telegram():
    try:
        telegram = "https://api.telegram.org/bot" + API_KEY + "/getUpdates"
        status = requests.get(telegram)
        parser = json.loads(status)
        Chat_ids.append(parser["id"])
        print(Chat_ids)

    except:
        print("api key error")
        print(status)

def sendmsg(text, chat_id):
    url_req = "https://api.telegram.org/bot" + API_KEY + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    requests.get(url_req)

def email(message):
    print()


def main():
    cycle = 0
    while(True):
        cycle = cycle + 1
        driver.get(url)
        sleep(5)
        check()
        driver.close
        print(cycle)
        sleep(300)

if __name__ == "__main__":
    main()
