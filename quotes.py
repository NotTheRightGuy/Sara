import requests
from bs4 import BeautifulSoup
import random

def give_me_a_random_quote():
    """

    :return: A random quote of the day from internet
    """
    url = 'https://www.brainyquote.com/quote_of_the_day'
    website = requests.get(url)
    soup = BeautifulSoup(website.text,'lxml')

    quotes  = soup.findAll('div',class_='clearfix')

    quotes_list = []
    for a in quotes:
        quotes_list.append(a.text.split("  "))

    return (random.choice(quotes_list)[0])
