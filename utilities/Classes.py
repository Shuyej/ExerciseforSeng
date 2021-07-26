import requests
from bs4 import BeautifulSoup as bs
import re  # pass this library as it has variables which we will use
from PIL import Image  # import PIL function from library Image #libraries defined outside the class
from abc import ABC, abstractmethod

class links(ABC): #add ABC to links to make sure it is the abstract class
    #initially passed four different variables which is illogical since each URL should be a object
    def __init__(self, URL):
          self.URL = str(URL) #Any of the derive classes should expect URL
    @abstractmethod
    def getlinks(self, soup): #page and soup are defined in the main body and passed down to be executed by function for function to work
        pass

    @abstractmethod
    def getimages(self, soup):
        pass

class BBC(links):
    def getlinks(self, soup):
        pass

    def getimages(self, soup):
        pass

class Sky(links):
    def getlinks(self, soup):
        pass

    def getimages(self, soup):
        pass
class Fox(links):
    def getlinks(self, soup):
        pass

    def getimages(self, soup):
        pass
class AlJazeera(links):
    def getlinks(self, soup):
        pass

    def getimages(self, soup):
        pass


    def getimages(self, soup):
        images = soup.select('img') # select used as it is better to find a wider range of image sources. find_all mostly restricted to jpg or http.
        #find_all is not the only way to attain image links
        self.image_links = []
        for image in images: #added get src to find src of image. or else as seen in line 17, it will not work
                image_source = image.get('src') #find src for each element, so being more specific, which wasnt the case when using find_all
                if not image == "None": #prints out elements which are not none. Thus these image are elements of images which is of our interest
                    self.image_links.append(image_source) #image_links alone isnt recognised as a variable
                  # update array image_links with each images available for each of the websuites looked at
        #image_links.append() does the following; it is defined outside, but added to the for loop, and thus edited with updated elements
        #then we want to print out or return results so we use return image_links
                if not image.startwith('http'):
                    self.image_links.append("https" + image_source)
        return self.image_links #values you want returned from the links function #Edit

#image_links returns all list
#image_links_first returns first element only
#It is not possible to conver non-http tags to jpg. But for websites that miss http tag only, we can add http to fix the error, and convert jpg files to http. In a way, we just implement them to http, not convert. There is a difference.

# The logic of what I am doing here is to develop a function to produce the links to images and URLS.
# How I am doing it is using for loops that sotrs each and every link, for a given URL as defined in main
# Why I am designing functions is to ensure my codes are scalable for different urls