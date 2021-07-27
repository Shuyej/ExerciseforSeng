import requests
from bs4 import BeautifulSoup as bs
import re  # pass this library as it has variables which we will use
from PIL import Image  # import PIL function from library Image #libraries defined outside the class

class links(): #add brackets to class
    #initially passed four different variables which is illogical since each URL should be a object
    def __init__(self, URL): #want to print out all the initial statements in the initialiser, and the statements inform us all the URLs in our code
          self.URL = str(URL)   #Declare URLS here as I want to use them in the program #And I want to specify which URL refers to which link

#Use string since our URL are string
#Inside init, otherwise known as the constructor we declare the global variables
#URL is a global variable, and each of its elements are specified so it is globally know what its element implies

    def getlinks(self, soup): #page and soup are defined in the main body and passed down to be executed by function for function to work
        atag = soup.find_all('a')  # Never add this inside the for loop to be able to reuse soup.find_all('a)
        self.links = []  # reference --> What you can get back is where info
        print(len(atag)) #In the example below, we print len(atag) to find out number of elements passed
#Only variable soup is passed as it is used

        for obj in atag:
            href = obj.get('href') ##inside for loops we return variables
            print(href); #exit()

a = links('https://www.bbc.co.uk/sport/football/57796830')
page = requests.get(a.URL)  # 0 and variable #address bar
soup = bs(page.content, 'html.parser')

a.getlinks(soup)


