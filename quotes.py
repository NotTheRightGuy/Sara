import requests
from bs4 import BeautifulSoup
import random


def give_me_a_random_quote():
    """

    :return: A random quote of the day from internet
    """
    url = 'https://www.brainyquote.com/quote_of_the_day'
    website = requests.get(url)
    soup = BeautifulSoup(website.text, 'lxml')

    quotes = soup.findAll('div', class_='clearfix')

    quotes_list = []
    for a in quotes:
        quotes_list.append(a.text.split("  "))

    quote_full = random.choice(quotes_list)[0]

    quote_full = quote_full.split('\n')
    quote = quote_full[1]
    author = quote_full[3]

    return quote, author


def quote_decorator(quote, author):
    cs = len(quote) // 2
    print("=" * cs, "Quote of the Day", "=" * cs)
    print(quote)
    print(author.center(16 + (cs * 2)))
    print("=" * cs, "=" * 16, "=" * cs)
