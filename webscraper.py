import requests
from bs4 import BeautifulSoup

def scrape(url, tag):
    response = requests.get(url)
    # print(response.text)

    soup = BeautifulSoup(response.text, 'html.parser')
    # print (soup.prettify())
    try:
        for txt in soup.find_all(tag):
            print(txt.getText())
    except:
        print("Invalid parameters")


url = input("Enter the url of website: ")
tag = input("Enter the tag of element: ")
scrape(url, tag)