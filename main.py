import requests
from bs4 import BeautifulSoup as bs

def main():
    import requests
    from bs4 import BeautifulSoup as bs
    print("start program")

    URLs = ['https://www.bbc.co.uk/', 'https://news.sky.com/uk', 'https://www.foxnews.com/', 'https://www.aljazeera.com/']
    page = requests.get(URLs)
    soup = bs(page.content, 'html.parser')

    atag = soup.find_all('a')  # Never add this inside the for loop to be able to reuse soup.find_all('a)
    for link in atag:  # focus on 'a' tag where each elment is refered to as link
        href = link.attrs['href']
        Dict = {'https://www.bbc.co.uk/': href, 'https://news.sky.com/uk': href, 'https://www.foxnews.com/': href, 'https://www.aljazeera.com/': href}  # URLS to be extracted from the 4 websites
        for key, value in Dict.items():
            print(key, value)


    atag = soup.find_all('a')  #Never add this inside the for loop to be able to reuse soup.find_all('a)
    links = [] #stores all links
    for link in atag: #focus on 'a' tag where each elment is refered to as link
        links.append(link.get('href')) #update our array with elements being link, with link being URL as defined by 'get'
    # #Now that information is stored on links we next print out the respective elements or data
    for link in links: #print out elements within array links
        print(link) #print each link #since last for loop updates the links, with link, we know print these elements
    print("\n")


    print("end program")

if __name__ == "__main__":
    main()