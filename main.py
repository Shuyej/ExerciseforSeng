import requests
from bs4 import BeautifulSoup as bs
import re

def main():
    import requests
    from bs4 import BeautifulSoup as bs
    print("start program")

    URLs = ['https://www.bbc.co.uk/', 'https://news.sky.com/uk', 'https://www.foxnews.com/', 'https://www.aljazeera.com/']
    dict = {}
    dict1 = {}

    for url in URLs:

        page = requests.get(url) #0 and variable
        soup = bs(page.content, 'html.parser')

        atag = soup.find_all('a')  # Never add this inside the for loop to be able to reuse soup.find_all('a)
        links = [] #reference --> What you can get back is where info

        for obj in atag:
            href = obj.get('href')

            if not href.startswith('http'):
                links.append(href)

        dict[url] = links

        print("'\n'")

        images = soup.find_all('img', {'src': re.compile('.jpg')})  # re.compiles finds src tag of img element, then creates a jpg file of them
        image_names_and_links = []

        for image in images:
            image_names_and_links.append(image['src'] + '\n')
            dict1[url] = image_names_and_links

    print(dict)
    print(dict1)


    print("end program")

if __name__ == "__main__":
    main()