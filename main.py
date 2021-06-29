
import requests
from bs4 import BeautifulSoup as bs

def main():
    print("start program")

    #URL = 'https://www.bbc.co.uk/'
    URLs = ['https://www.bbc.co.uk/', 'https://news.sky.com/uk', 'https://www.foxnews.com/', 'https://www.aljazeera.com/' ]
    usernewschannelchoice = input("Please choose which news channel links you would like to extract, choose between 0 to 3, with 0 = BBC, 1 = SKy, 2 = Fox News, 3 = Al Jazeera: ")
    page = requests.get(URLs[usernewschannelchoice])
    soup = bs(page.content, 'html.parser')
    #print(soup)
    links = []
    for link in soup.find_all('a'): #focus on a tag where links are store
        links.append(link.get('href')) #update date links[] with url
    for link in links:
        print(link) #print each link

    print("end program")

if __name__ == "__main__":
    main()