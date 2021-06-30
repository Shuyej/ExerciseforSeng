import requests
from bs4 import BeautifulSoup as bs
import re

def main():
    print("start program")

    URLs = ['https://www.bbc.co.uk/', 'https://news.sky.com/uk', 'https://www.foxnews.com/', 'https://www.aljazeera.com/']
    dictofURLlinks = {}
    dictofimagelinks = {}

    for url in URLs:

        page = requests.get(url) #0 and variable
        soup = bs(page.content, 'html.parser')

        atag = soup.find_all('a')  # Never add this inside the for loop to be able to reuse soup.find_all('a)
        links = [] #reference --> What you can get back is where info

        for obj in atag:
            href = obj.get('href')

            if not href.startswith('http'):
                links.append(href)

        dictofURLlinks[url] = links #This means in the dictionary dictofURLlinks, the identifier is url, and we update it with links

        images = soup.find_all('img', {'src': re.compile('http')})  # re.compiles finds src tag of img element, then creates a http of them
        image_links = []

        for image in images:
            image_links.append(image['src']) #update array image_links with each images available for each of the websuites looked at

        dictofimagelinks[url] = image_links

    print(dictofURLlinks)
    print(dictofimagelinks)

    print("end program")
if __name__ == "__main__":
    main()