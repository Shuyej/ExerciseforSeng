import requests
from bs4 import BeautifulSoup as bs

class links:
    import re  # pass this library as it has variables which we will use
    from PIL import Image  # import PIL function from library Image
    #initially passed four different variables which is illogical since each URL should be a object
    def __init__(self, URL): #want to print out all the initial statements in the initialiser, and the statements inform us all the URLs in our code
          self.URL = str(URL)   #Declare URLS here as I want to use them in the program #And I want to specify which URL refers to which link

#Use string since our URL are string
        #Inside init, otherwise known as the constructor we declare the global variables
        #URL is a global variable, and each of its elements are specified so it is globally know what its element implies


    def getlinks(self, soup): #page and soup are defined in the main body and passed down to be executed by function for function to work
        atag = soup.find_all('a')  # Never add this inside the for loop to be able to reuse soup.find_all('a)
        self.links = []  # reference --> What you can get back is where info
#Only variable soup is passed as it is used

        for obj in atag:
            href = obj.get('href') ##inside for loops we return variables

            if href.startswith('http'): #http is a string
                self.links.append(href) #despite links being defined outside the for loop, we add it inside, thus the variable is considered inside for loop

                if not href.startwith('http'): #added if statement to consider http, so for objects with no http elements we add http
                    self.links.append("https" + href) #even if self.links not defined within for loop, so not noticed as a for loop variable
                    #self.links is a local function so it is updated within the function

        return self.links #self.links was created as a local variable even if it wasnt passed in the paranthesis
    #usually passing through the paranthesis is a way to declare local variables
    #self.x is key for classes to recognise functions

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