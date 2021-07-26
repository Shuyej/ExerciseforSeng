import requests
from bs4 import BeautifulSoup as bs
import utilities.Classes #new library replacing utilities.core

def main():
    print("start program")

    dictofURLlinks = {} #defined here so information stored, but it is stored to ensure we access each NEW element
    dictofimagelinks = {} #defined here so information stored, but it is stored to ensure we access each NEW element

    #URLs = ['https://www.bbc.co.uk/', 'https://news.sky.com/uk', 'https://www.foxnews.com/','https://www.aljazeera.com/']  # Notice self.URLS is key to utilise the variable

    #for url in URLs:
#No longer can write classes.links since links is a abstract class. We only want to use the base class.
#There is the possibility of using base class and sub class, but once abstract classes are in the picture, we can only use sub classes
    BBCnewsobj = utilities.Classes.BBC('https://www.bbc.co.uk/')
    Skynewsobj = utilities.Classes.Sky('https://news.sky.com/uk')
    Foxnewsobj = utilities.Classes.Fox('https://www.foxnews.com/')
    AlJazeeranewsobj = utilities.Classes.AlJazeera('https://www.aljazeera.com/')
#So, each links are passed through the class link, storing them as variables of that class
#Above store the URL links in a global variable refered to as URL

    page = requests.get(BBCnewsobj.URL)  #make it clear you want the URL of the object
    soup = bs(page.content, 'html.parser')

    dictofURLlinks[BBCnewsobj]= BBCnewsobj.getlinks(soup) #How to link classes  # This means in the dictionary dictofURLlinks, the identifier is url, and we update it with links
    dictofimagelinks[BBCnewsobj]= BBCnewsobj.getimages(soup)#How to link classes  #store function links values inside dictofImagelinks,for each url,but note where you store values has been assigned as a {} thus, you store values as a dictionary

    print(dictofURLlinks)
    print(dictofimagelinks)
   #Below is a ty error example
    #for url in URLs:
     #   try:
           # print(dictofURLlinks[url][300]) #i.e. dictname["element name"]
            #print(dictofimagelinks[url][30]) #returns bbc only. Can remove bbc to print all keys
    #functions return all elements, it is only in main you specify which elements you want
      #  except Exception:
           # print("Index out of range for " + url)


    print("end program")
if __name__ == "__main__":
    main() #ensures anything written in the main function is printed, and two print files from the packages Linktowebsites and Linkstoimages, important to import them else you have to use print(filename.__name__)

    # A module can define functions, classes, and variables.
    #So when the interpreter runs a module, the __name__ variable will be set as  __main__ if the module that is being run is the main program.
    #But if the code is importing the module from another module, then the __name__  variable will be set to that module’s name.

# The logic of what I am doing here is to store links but for each URL which are known as the key, and for each key there are values which are links
# How I am doing it is through dicts and for loop to be able to access each URL
# Why I am using Dicts is because each identifier is unique with values, so it easier for clarity purposes to say what representes each identifier, where values represent identifier for which we want to be links to images and links to URLS


#print out the keys of a dictionary
#print out the first values of a list
#then classes then abstract classes