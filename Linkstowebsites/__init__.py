
import requests
from bs4 import BeautifulSoup as bs
import re

def links(page,soup):

    atag = soup.find_all('a')  # Never add this inside the for loop to be able to reuse soup.find_all('a)
    links = []  # reference --> What you can get back is where info

    for obj in atag:
        href = obj.get('href')

        if not href.startswith('http'):
            links.append(href)

    return links #values you want returned from the links function

