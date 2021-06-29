
import requests
from bs4 import BeautifulSoup as bs

def main():
    print("start program")
    URL = 'https://www.bbc.co.uk/'
    page = requests.get(URL)
    soup = bs(page.content, 'html.parser')

    print("end program")

if __name__ == "__main__":
    main()