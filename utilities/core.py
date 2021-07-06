import re #pass this library as it has variables which we will use
from PIL import Image #import PIL function from library Image

def getlinks(soup): #page and soup are defined in the main body and passed down to be executed by function for function to work
    atag = soup.find_all('a')  # Never add this inside the for loop to be able to reuse soup.find_all('a)
    links = []  # reference --> What you can get back is where info
#Only variable soup is passed as it is used

    for obj in atag:
        href = obj.get('href') ##inside for loops we return variables

        if href.startswith('http'): #http is a string
            links.append(href) #despite links being defined outside the for loop, we add it inside, thus the variable is considered inside for loop

    return links #values you want returned from the links function
#You dont have to return anything inside for loop, but the variable of interest. That variable has values of interest.

def getimages(soup):
        images = soup.select('img')  # select used as it is better to find a wider range of image sources. find_all mostly restricted to jpg or http.
        #find_all is not the only way to attain image links
        image_links = []

        for image in images: #added get src to find src of image. or else as seen in line 17, it will not work
                image_source = image.get('src') #find src for each element, so being more specific, which wasnt the case when using find_all
                image_links.append(image_source)  # update array image_links with each images available for each of the websuites looked at
        #image_links.append() does the following; it is defined outside, but added to the for loop, and thus edited with updated elements
        #then we want to print out or return results so we use return image_links
        return image_links #values you want returned from the links function
