from bs4 import BeautifulSoup
import requests
import time

url = 'http://weheartit.com/inspirations/taylorswift?scrolling=true&page=1&before=162206459'
def get_images(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    imges = soup.select('img.entry-thumbnail')
    for i in imges:
        img_url.append(i.get('src'))

img_url = []
links = []

def get_pages(num):
        for i in range(0,num):
            url = 'http://weheartit.com/inspirations/taylorswift?scrolling=true&page={}&before=162206459'.format(i)
            links.append(url)
        print links

get_pages(2)

for l in links:
    get_images(l)

print (img_url)