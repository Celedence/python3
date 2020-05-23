# https://quotes.toscrape.com

import requests
from bs4 import BeautifulSoup
from csv import writer
from time import sleep
from random import choice
from csv import DictReader

BASE_URL = "http://quotes.toscrape.com"

def read_quotes(filename):
    with open(filename, "r") as file:
        csv_reader = DictReader(file)
        return list(csv_reader)


def start_game(quotes):
    quote = choice(quotes)
    remaining_guesses = 4
    print("Here's a quote: ")
    print(quote["text"])
    print(quote["author"])
    guess = ''
    while guess.lower() != quote["author"].lower():
        guess = input(f"Who said this quote? Guesses remaining {remaining_guesses}\n ")
        if guess.lower() == quote["author"].lower():
            print("You got it right genius!")
            break
        remaining_guesses -= 1
        if remaining_guesses ==  3:
            res = requests.get(f"{BASE_URL}{quote['bio_link']}")
            soup = BeautifulSoup(res.text, "html.parser")
            birth_date = soup.find(class_="author-born-date").get_text()
            birth_place = soup.find(class_="author-born-location").get_text()
            print(f"Here's a hint: The author was born in {birth_place} on {birth_date}")
        elif remaining_guesses ==2:
            print(f"Here's a hint: The author's first name starts with: {quote['author'][0]}")
        elif remaining_guesses ==1:
            last_initial = quote['author'].split(" ")[1][0]
            print(f"Here's a hint: The author's last name starts with: {last_initial}")
        else :
            print(f"Sorry you ran out of guesses. The answer was {quote['author']}")

    again = ''
    while again.lower() not in ('y', 'n', 'yes', 'no'):        
        again = input("Would you like to play again (y/n)?")
    if again.lower() in ('yes','y'):
        print("Ok play again")
        sleep(2)
        return start_game(quotes)
    else:
        print("Ok, Goodbye")


quotes = read_quotes("quotes.csv")
# quotes = scrape_quotes()
start_game(quotes)