# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import time

url = 'http://wh.xiaozhu.com/fangzi/2739731663.html'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Cookie':'abtest_ABTest4SearchDate=b; xzuuid=02f6b7b4; newcheckcode=ec388225313a09329923283bce3fd7ca; xzuinfo=%7B%22user_id%22%3A8727868563%2C%22user_name%22%3A%2213438993989%22%2C%22user_key%22%3A%22f9e92070fd%22%7D; xzucode=30aa9fcdaf19096819fd8af94f084840; xzucode4im=5ec2e048d693bb2ca10cfb59854e1288'
}

def get_attractions(url,data=None):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    title = soup.select('div.pho_info > h4 > em')[0].text
    address = soup.select('span.pr5')[0].text.rstrip()
    price = soup.select('div.day_l > span')[0].text
    img = soup.select('div.member_pic > a > img')[0].get('src')
    gender = soup.select('div.member_pic > div')[0].get('class')[0]

    data = {
        'title':title,
        'address':address,
        'price':price,
        'img':img,
        'gender':print_gender(gender)
    }

    print data
'''
    print (type(address))
    print (address)
    print (price)
    print (img)
    print (gender)
'''

def print_gender(class_name):
    if class_name == 'member_ico1':
        return ('female')
    elif class_name ==  'member_ico':
        return ('male')

link_list = []

def get_links(page_num):
    for i in range(0,page_num):
        full_url = 'http://wh.xiaozhu.com/search-duanzufang-p{}-0/'.format(i)
        wb_data = requests.get(full_url)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        for link in soup.select('a.resule_img_a'):
            link_list.append(link.get('href'))




print (link_list)



get_links(2)

for l in link_list:
    get_attractions(l)