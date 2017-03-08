from bs4 import BeautifulSoup
import requests
import pymongo

client = pymongo.MongoClient('192.168.18.51',27017)
ganji = client['ganji']
urls = ganji['urls']

def get_cate_url():
	url_list = []
	wb_page = requests.get('http://cd.ganji.com/wu/')
	soup = BeautifulSoup(wb_page.text,'lxml')
	for i in soup.select(('dl.fenlei > dt > a')):
		url_list.append('http://cd.ganji.com' + i.get('href'))
	for u in url_list:
		data = {
			'url':u
		}
		urls.insert_one(data)

#get_cate_url()

#urls.delete_one({'url':'http://cd.ganji.com/wupinjiaohuan/'})
