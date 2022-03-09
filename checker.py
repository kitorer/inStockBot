import json
from posixpath import abspath
import smtplib
import urllib.request
from datetime import datetime
from bs4 import BeautifulSoup
from email.message import EmailMessage

log = ""

# Boolean: returns true if word is found in the url
def isInStock(url, word):
    global log
    try:
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, features= 'html.parser')
        print(page.read())

        if word in soup.text:
            return True
        return False
    except:
        log += "Error parsing url"

def main():
    print("This works on non js sites")
    url = input("site to check ")
    keyword = input("item ")
    available = isInStock(url,keyword)

    if available:
        print("found!")
    else:
        print("not found!")

if __name__ == "__main__":
    main()
