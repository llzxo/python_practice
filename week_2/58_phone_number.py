from bs4 import BeautifulSoup
import requests
import pymongo

client = pymongo.MongoClient('192.168.18.51',27017)
llzxo = client['llzxo']
phone_number = llzxo['phone_number']

def yes_no(url):
	wb_page = requests.get(url)
	soup = BeautifulSoup(wb_page.text,'lxml')
	count = soup.select('span > b')[0].text
	if int(count) == 0:
		print ('false')
	else:
		print ('true')

def get_info(url):
	wb_page = requests.get(url)
	soup = BeautifulSoup(wb_page.text,'lxml')
	count = soup.select('span > b')[0].text
	if int(count) == 0:
		pass
	else:
		titles = soup.select('strong.number')
		links = soup.select('li > a.t')
		print len(titles)
		print len(links)
		for title ,link in zip(titles,links):
			data = {
				'title' : title.text,
				'link':link.get('href')
			}
			phone_number.insert_one(data)
			print (data)

def get_page(num):
	url_list = []
	for i in range(1,num):
		url = 'http://cd.58.com/shoujihao/pn{}/'.format(i)
		url_list.append(url)
	return url_list

#urls = get_page(120)
#for u in urls:
#	get_info(u)

#count = 0
#for i in phone_number.find():
#	count += 1
#print count
