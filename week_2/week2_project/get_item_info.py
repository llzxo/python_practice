from bs4 import BeautifulSoup
import requests
import pymongo
import time
import random

headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
	'Connection':'Keep-alive',
	'Cookie':'ganji_uuid=3736657222827255549431; ganji_xuuid=fd5f3778-8f71-40eb-e5ea-0fa50c583a72.1488766156685; webimverran=24; als=0; citydomain=cd; crawler_uuid=148897775291774200151364; GANJISESSID=d241d09d6fd14d643b440651157b3b16; _gj_txz=MTQ4ODk3ODM2MjrF5Bwgo9LbJ4mngt7XQvqCiA29IQ==; lg=1; 58uuid=069ff99e-c75e-4460-a69b-9315693d5852; new_session=0; init_refer=; new_uv=8; ganji_login_act=1488977782027; webimUserId=4045669753%3A%3A2592000%3A%3A1488977782; webimCometActiveTime=1488977790729%3A%3Aundefined%3A%3A1488977790; webimCometPageMark=0.3159010083007452%3A%3Aundefined%3A%3A1488977790; _gl_tracker=%7B%22ca_source%22%3A%22-%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A75354776900%7D; webimLastRecvUserStatussTime=1488977865283%3A%3A180000%3A%3A1488977865; webimNeedComet=4045669753%3A%3A172800%3A%3A1488977865; webimCometExistTime=1488977865320%3A%3A10%3A%3A1488977865'
}

proxy_list = [
	'http://125.88.74.122:83',
	'http://121.199.25.64:81',
	'http://120.27.113.72:8888'
]
proxy_ip = random.choice(proxy_list)
proxies = {'http':proxy_ip}

client = pymongo.MongoClient('192.168.18.51',27017)
ganji = client['ganji']
items = ganji['items']
urls = ganji['urls']
item_links = ganji['item_links']

url_list = []
for u in urls.find():
	url_list.append(u['url'])

def get_item_link(input,num):
	for i in range(1,num):
		url = input + 'o{}'.format(i)
		time.sleep(2)
		print url
		wb_data = requests.get(url,headers=headers)
		soup = BeautifulSoup(wb_data.text,'lxml')
		#if soup.find('a.ft-tit'):
		if soup.find('div',attrs={'class':'pageBox'}):
			zhuanzhuan = soup.find('a',attrs={'class':'ft-tit'}) #zhuanzhuan or normal page
			links = soup.select('li.js-item > a.ft-tit') if zhuanzhuan!=None else soup.select('td.t > a.t')
			#elif soup.find('a.t'):
			#	links = soup.select('a.t')
			for link in links:
				data={
					'link':link.get('href')
				}
				item_links.insert_one(data)
				print data
		else:
			pass

def get_item_info(url):
	wb_data = requests.get(url)
	soup = BeautifulSoup(wb_data.text,'lxml')
	soup.find('a.ft-tit')
	title = soup.select('h1.title-name')
	date = soup.select('i.pr-5')
	cate = soup.select('ul.det-infor > li > span > a')
	price = soup.select('i.f22')
	region = soup.select('ul.det-infor > li > a')
	new = soup.select('ul.second-det-infor > li')
	print (len(region))
	data = {
		'title':title[0].text if len(title)!=0 else None,
		'date':date[0].text.strip() if len(date)!=0 else None,
		'cate':cate[0].text if len(cate)!=0 else None,
		'price':price[0].text if len(price)!=0 else None,
		'region':region[2].text if len(region)==3 else None ,
		'new':new[0].text if len(new) != 0 else None
		#'title':title,
		#'date':date,
		#'cate':cate,
		#'price':price,
		#'region':region,
		#'new':new
	}
	#items.insert_one(data)
	print data

#print url_list
#get_item_link('http://cd.ganji.com/jiaju/',100)
#get_item_info('http://cd.ganji.com/jiaju/2423463300x.htm')
for u in url_list:
	get_item_link(u,60)

#count = 0
#for l in item_links.find():
#	if count %5 ==0:
#		time.sleep(1)
#	else:
#		print (l["link"])
#		get_item_info(l["link"])
#	count+=1

#begin:15:20
#end:16:25
#count : 96779