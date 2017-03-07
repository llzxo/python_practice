from bs4 import BeautifulSoup

with open('../Plan-for-combating-master/week1/1_2/1_2answer_of_homework/1_2_homework_required/index.html','r') as wb_data:
    Soup = BeautifulSoup(wb_data,'lxml')
    images = Soup.select('body > div:nth-of-type > div > div.col-md-9 > div:nth-of-type  > div:nth-of-type > div > img')
#    price = Soup.select('body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(1) > div > div.caption > h4.pull-right')
#    name = Soup.select('body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(1) > div > div.ratings > p.pull-right')








'''
(image:	body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(1) > div > img)
(price:	body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(1) > div > div.caption > h4.pull-right)
(name:	body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(1) > div > div.caption > h4:nth-child(2) > a)
(body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(1) > div > div.ratings > p.pull-right)
(body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(1) > div > div.ratings > p:nth-child(2) > span:nth-child(1))
'''
