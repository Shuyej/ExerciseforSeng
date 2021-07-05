
import requests
from bs4 import BeautifulSoup as bs
import re

def links(page,soup):
        images = soup.find_all('img', {
            'src': re.compile('http')})  # re.compiles finds src tag of img element, then creates a http of them
        image_links = []

        for image in images:
            image_links.append(
                image['src'])  # update array image_links with each images available for each of the websuites looked at

        return image_links #values you want returned from the links function


