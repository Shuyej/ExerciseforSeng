import requests
from bs4 import BeautifulSoup as bs
import re
import Linkstowebsites
import LinkstoImages

def main():
    print("start program")

    URLs = ['https://www.bbc.co.uk/', 'https://news.sky.com/uk', 'https://www.foxnews.com/', 'https://www.aljazeera.com/']
    dictofURLlinks = {}
    dictofimagelinks = {}

    for url in URLs:

        page = requests.get(url) #0 and variable
        soup = bs(page.content, 'html.parser')

        dictofURLlinks[url] = Linkstowebsites.links(page,soup)  # This means in the dictionary dictofURLlinks, the identifier is url, and we update it with links
        dictofimagelinks[url] = LinkstoImages.links(page,soup)

    print(dictofURLlinks)
    print(dictofimagelinks)

    print("end program")

if __name__ == "__main__":
    main()

    # A module can define functions, classes, and variables.
    #So when the interpreter runs a module, the __name__ variable will be set as  __main__ if the module that is being run is the main program.
    #But if the code is importing the module from another module, then the __name__  variable will be set to that module’s name.
