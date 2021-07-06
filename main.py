import requests
from bs4 import BeautifulSoup as bs
import utilities.core

def main():
    print("start program")

    URLs = ['https://www.bbc.co.uk/', 'https://news.sky.com/uk', 'https://www.foxnews.com/', 'https://www.aljazeera.com/']
    dictofURLlinks = {}
    dictofimagelinks = {}

    for url in URLs:
        page = requests.get(url) #0 and variable
        soup = bs(page.content, 'html.parser')

        dictofURLlinks[url] = utilities.core.getlinks(soup)  # This means in the dictionary dictofURLlinks, the identifier is url, and we update it with links
        dictofimagelinks[url] = utilities.core.getimages(soup)  #store function links values inside dictofImagelinks,for each url,but note where you store values has been assigned as a {} thus, you store values as a dictionary
    #links is the function name, not the 'return value' variable name!!
    print(dictofURLlinks)
    print(dictofimagelinks)

    print("end program")

if __name__ == "__main__":
    main() #ensures anything written in the main function is printed, and two print files from the packages Linktowebsites and Linkstoimages, important to import them else you have to use print(filename.__name__)
    #A module can define functions, classes, and variables.
    #So when the interpreter runs a module, the __name__ variable will be set as  __main__ if the module that is being run is the main program.
    #But if the code is importing the module from another module, then the __name__  variable will be set to that module’s name.
