import requests
from bs4 import BeautifulSoup
import re 
import pandas as pd 


def link_scraper():
    baseURL = input("Enter the URL: ")
    get_url = requests.get(baseURL)
    soup = BeautifulSoup(get_url.text, 'html.parser')

    tags = soup.find_all('a', attrs={'href': re.compile("^http")})

    urlAddress = []
    urlName = []
    for link in tags:
        # print(f"{link.string}  - {link.get('href')}")
        urlName.append(link.string)
        urlAddress.append(link.get("href"))
    df = pd.DataFrame(zip(urlName, urlAddress), columns=['Name', 'Link'])
    df.to_csv("link_scraper.csv")
    print("Done!!!")

link_scraper()    