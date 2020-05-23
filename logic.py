#  https://quotes.toscrape.com

import requests
from bs4 import BeautifulSoup
from csv import writer
from time import sleep
from random import choice
from csv import DictWriter


BASE_URL = "http://quotes.toscrape.com"


def scrape_quotes():
    all_quotes = []
    url = "/page/1"
    while url:
        response = requests.get(f"{BASE_URL}{url}")
        # print(f"Now scraping {BASE_URL}{url}")
        soup = BeautifulSoup(response.text,"html.parser")
        quotes = soup.find_all(class_="quote")

        for quote in quotes:
            all_quotes.append({
                "text":quote.find(class_="text").get_text(),
                "author":quote.find(class_="author").get_text(),
                "bio_link":quote.find("a")["href"]
            })
        next_btn = soup.find(class_="next")
        url = next_btn.find("a")["href"] if next_btn else None
#     sleep(2)
    return all_quotes
#     print("Scrape complete")
#     sleep(2)
# print("Compiling")
# sleep(2)
# print(all_quotes)
quotes = scrape_quotes()

with open("quotes.csv", "w") as file:
    headers = ["text","author","bio_link"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writerheader()
    for quote in quotes:
        csv_writer.writerow(quotes)
    

   