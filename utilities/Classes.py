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
    def getlinks(self, soup): #soup is only passed as it is used later
        atag = soup.find_all('a')  # Never add this inside the for loop to be able to reuse soup.find_all('a)
        self.links = []  #

        for obj in atag:
            href = obj.get('href')  ##inside for loops we return variables

            if href.startswith('http'):  # http is a string
                self.links.append(href)  # despite links being defined outside the for loop, we add it inside, thus the variable is considered inside for loop

            if not href.startswith('http'):   #elif is used in Python not elseif
                self.links.append("https://search.bbc.co.uk/search"+ href) #note if you have x + z then there will be a space

        return self.links  # self.links was created as a local variable even if it wasnt passed in the paranthesis

    def getimages(self, soup):
        images = soup.select('img')  # select used as it is better to find a wider range of image sources. find_all mostly restricted to jpg or http.
        # find_all is not the only way to attain image links
        self.image_links = []

        for image in images:  # added get src to find src of image. or else as seen in line 17, it will not work
            image_source = image.get('src')  # find src for each element, so being more specific, which wasnt the case when using find_all

            if not image == "None":  # prints out elements which are not none. Thus these image are elements of images which is of our interest
                self.image_links.append(image_source)  # image_links alone isnt recognised as a variable


            #if not image.startwith('http'):
                #self.image_links.append("https" + image_source)
            #line 45 and 46 will not run as you cant add http elements to jpg files

        return self.image_links  # values you want returned from the links function #Edit

class Sky(links):
    def getlinks(self, soup):
        atag = soup.find_all('a')  # Never add this inside the for loop to be able to reuse soup.find_all('a)
        self.links = []  #

        for obj in atag:
            href = obj.get('href')  ##inside for loops we return variables

            if href.startswith('http'):  # http is a string
                self.links.append(href)  # despite links being defined outside the for loop, we add it inside, thus the variable is considered inside for loop

            if not href.startswith('http'):
                self.links.append("https://skynews.com/" +href) #extract links where http is not added

        return self.links  # self.links was created as a local variable even if it wasnt passed in the paranthesis

    def getimages(self, soup):
        images = soup.select('img')  # select used as it is better to find a wider range of image sources. find_all mostly restricted to jpg or http.
        self.image_links = []
        for image in images:  # added get src to find src of image. or else as seen in line 17, it will not work
            image_source = image.get('src')  # find src for each element, so being more specific, which wasnt the case when using find_all

            if not image == "None":  # prints out elements which are not none. Thus these image are elements of images which is of our interest
                self.image_links.append(image_source)  # image_links alone isnt recognised as a variable

            # if not image.startwith('http'):
            # self.image_links.append("https" + image_source)
            # line 45 and 46 will not run as you cant add http elements to jpg files

        return self.image_links  # values you want returned from the links function #Edit


class Fox(links):
    def getlinks(self, soup):
        atag = soup.find_all('a')  # Never add this inside the for loop to be able to reuse soup.find_all('a)
        self.links = []  #

        for obj in atag:
            href = obj.get('href')  ##inside for loops we return variables

            if href.startswith('http'):  # http is a string
                self.links.append(
                    href)  # despite links being defined outside the for loop, we add it inside, thus the variable is considered inside for loop
        return self.links  # self.links was created as a local variable even if it wasnt passed in the paranthesis

    def getimages(self, soup):
        images = soup.select(
            'img')  # select used as it is better to find a wider range of image sources. find_all mostly restricted to jpg or http.
        for image in images:  # added get src to find src of image. or else as seen in line 17, it will not work
            image_source = image.get(
                'src')  # find src for each element, so being more specific, which wasnt the case when using find_all

            if not image == "None":  # prints out elements which are not none. Thus these image are elements of images which is of our interest
                self.image_links.append(image_source)  # image_links alone isnt recognised as a variable

            # if not image.startwith('http'):
            # self.image_links.append("https" + image_source)
            # line 45 and 46 will not run as you cant add http elements to jpg files

        return self.image_links  # values you want returned from the links function #Edit

class AlJazeera(links):
    def getlinks(self, soup):
        atag = soup.find_all('a')  # Never add this inside the for loop to be able to reuse soup.find_all('a)
        self.links = []  #

        for obj in atag:
            href = obj.get('href')  ##inside for loops we return variables

            if href.startswith('http'):  # http is a string
                self.links.append(
                    href)  # despite links being defined outside the for loop, we add it inside, thus the variable is considered inside for loop
        return self.links  # self.links was created as a local variable even if it wasnt passed in the paranthesis

    def getimages(self, soup):
        images = soup.select(
            'img')  # select used as it is better to find a wider range of image sources. find_all mostly restricted to jpg or http.
        for image in images:  # added get src to find src of image. or else as seen in line 17, it will not work
            image_source = image.get(
                'src')  # find src for each element, so being more specific, which wasnt the case when using find_all

            if not image == "None":  # prints out elements which are not none. Thus these image are elements of images which is of our interest
                self.image_links.append(image_source)  # image_links alone isnt recognised as a variable

            # if not image.startwith('http'):
            # self.image_links.append("https" + image_source)
            # line 45 and 46 will not run as you cant add http elements to jpg files

        return self.image_links  # values you want returned from the links function #Edit
