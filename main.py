import requests
from bs4 import BeautifulSoup as bs
import utilities.Classes #new library replacing utilities.core

def main():
    print("start program")

    dictofBBCURLlinks = {} #defined here so information stored, but it is stored to ensure we access each NEW element
    dictofBBCimagelinks = {} #defined here so information stored, but it is stored to ensure we access each NEW element

    URLs = ['https://www.bbc.co.uk/', 'https://news.sky.com/uk', 'https://www.foxnews.com/',
       'https://www.aljazeera.com/']  # Notice self.URLS is key to utilise the variable

    #for url in URLs:
    page = requests.get(URLs) #0 and variable
    soup = bs(page.content, 'html.parser')
    BBCnewsobj = utilities.Classes.links()   #define object to attain info of BBC News as it is a object of class links stored in utilities.classes package
    Skynewsobj = utilities.Classes.links()   #define object to attain info of Sky News as it is a object of class links stored in utilities.classes package
    Foxnewsobj = utilities.Classes.links()   #define object to attain info of Fox News as it is a object of class links stored in utilities.classes package
    AlJazeeranewsobj = utilities.Classes.links() #define object to attain info of Al Jazeera News as it is a object of class links stored in utilities.classes package

    dictofBBCURLlinks[BBCnewsobj]=  BBCnewsobj.getlinks(soup) #How to link classes  # This means in the dictionary dictofURLlinks, the identifier is url, and we update it with links
    dictofBBCimagelinks[URLs]['https://www.bbc.co.uk/'] =  BBCnewsobj.getimages(soup)#How to link classes  #store function links values inside dictofImagelinks,for each url,but note where you store values has been assigned as a {} thus, you store values as a dictionary

    print(dictofBBCURLlinks())
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