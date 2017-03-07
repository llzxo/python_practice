from bs4 import BeautifulSoup
import requests
import urllib2
import os
import re
import time

url = 'http://weheartit.com/inspirations/taylorswift?scrolling=true&page=1&before=162206459'
def get_images(url):
    # time.sleep(2)
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    imges = soup.select('img.main_img.img-hover')
    print imges
    for i in imges:
        img_url.append(i.get('src'))

img_url = []
links = []

def download(_url,name):
    if(_url==None):
        pass
    result = urllib2.urlopen(_url)
    if(result.getcode()!=200):
        pass
    else:
        data=result.read()
        with open(name,"wb") as code:
            code.wirte(data)
            code.close

def get_pages(num):
        for i in range(30,num,30):
            url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E6%9D%89%E6%A0%91%E5%8F%B6&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&word=%E6%9D%89%E6%A0%91%E5%8F%B6&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&fr=&pn={}&rn=30&'.format(i)
            links.append(url)
        print links

get_pages(120)
for l in links:
    get_images(l)
print img_url

count = 0
for address in img_url:
    if(address!=None):
        pathName="E:\\2333\\"+str(count+1)+".jpg"
        download(address,pathName)
        count = count + 1
        print "downloading:",count