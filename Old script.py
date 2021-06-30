import requests
from bs4 import BeautifulSoup as bs

def main():
    import requests
    from bs4 import BeautifulSoup as bs
    print("start program")
    #URL = 'https://www.bbc.co.uk/'
    URLs = ['https://www.bbc.co.uk/', 'https://news.sky.com/uk', 'https://www.foxnews.com/', 'https://www.aljazeera.com/' ] #URLS to be extracted from the 4 websites
    usernewschannelchoice = input("Please choose which news channel links you would like to extract, choose between 0 to 3, with 0 = BBC, 1 = SKy, 2 = Fox News, 3 = Al Jazeera: ")
    page = requests.get(URLs[int(usernewschannelchoice)]) #so user input considered as string #Note in progrsamming first element is considered 0
    #note that URLS are string type, so will user input, unless we specify user input is integer type
    soup = bs(page.content, 'html.parser')
    #print(soup)
    atag = soup.find_all('a')  #Never add this inside the for loop to be able to reuse soup.find_all('a)
    links = [] #stores all links
    for link in atag: #focus on 'a' tag where each elment is refered to as link
        links.append(link.get('href')) #update our array with elements being link, with link being URL as defined by 'get'
    # #Now that information is stored on links we next print out the respective elements or data
    for link in links: #print out elements within array links
        print(link) #print each link #since last for loop updates the links, with link, we know print these elements
    print("\n")


    userinput =input("Would you like to store the links in a text file? Enter Yes or No ")
    if userinput == "Yes":
        import requests
        from bs4 import BeautifulSoup as bs
        file = open("Link.txt", "w")  # if you have a word file, then it will not work. THen go on directory --> Exercise for Seng in this case where project was created --> should find a txt file
        URLs = ['https://www.bbc.co.uk/', 'https://news.sky.com/uk', 'https://www.foxnews.com/','https://www.aljazeera.com/']  # URLS to be extracted from the 4 websites
        print("You will need to change the URL for websites to be stored to different text file")
        page = requests.get(URLs[0])
        soup = bs(page.content, 'html.parser')
    atag = soup.find_all('a')  #Never add this inside the for loop to be able to reuse soup.find_all('a)
    links = [] #stores all links
    for link in atag: #focus on 'a' tag where each elment is refered to as link
        links.append(link.get('href')) #update our array with elements being link, with link being URL as defined by 'get'
    # #Now that information is stored on links we next print out the respective elements or data
    for link in links: #print out elements within array links
        print(link) #print each link #since last for loop updates the links, with link, we know print these elements
    print("\n")
    file.write(str(links))
    file.flush()
    file.close()


    print("end program")

if __name__ == "__main__":
    main()