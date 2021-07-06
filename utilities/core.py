import re #pass this library as it has variables which we will use
from os.path import basename, splitext
def getlinks(soup): #page and soup are defined in the main body and passed down to be executed by function for function to work
    atag = soup.find_all('a')  # Never add this inside the for loop to be able to reuse soup.find_all('a)
    links = []  # reference --> What you can get back is where info
#Only variable soup is passed as it is used

    for obj in atag:
        href = obj.get('href')

        if href.startswith('http'): #http is a string
            links.append(href)

    return links #values you want returned from the links function

def getimages(soup):
        #images = soup.find_all('img', {'src': re.compile('http')})  # re.compiles finds src tag of img element, then creates a http of them
        #find_all is not the only way to attain image links
        images = soup.select('img')
        image_links = []

        for image in images: #added get src to find src of image. or else as seen in line 17, it will not work
            image_source = (image.get(('src'))) # update array image_links with each images available for each of the websuites looked at
        #better to store recieved images inside a variable
        image_links.append(image_source)
        return image_links #values you want returned from the links function
