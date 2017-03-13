import requests
import urllib2

headers = {
	'Cookie':'NID=98=0RpAFAQRCgrxaaeo5TRdIMsVKY_Xx7xr2VtYH4kALKlm2m-IQZYfBwUmh8Dg3gjAM1zupFUAHjRVyKt9k4sgEjdH_B8JVlu2wbi5vYVcZXk520N9qRUX9w3dOo0JP0SgMm2Drsm6UidUj0imnJkVG18gdTR2TGuZkVblFRSwafQuLYF-Y6nXkreZg7bsuu4fGpObqAKBWL8sc5BSyeCuf4645zVFQKnx67-pNIeZYuKya2XaFpR5KX4qck-0qBnGA36nAOYRou4LrKs3vxNXRBQqpQAyRnRobo8aMcitirS3JySVKAQd7vvsDGO6TTN1IcGArpLVUrnvUQ5hk1I0uY4QV1aGZkGg0SviulJKDQPXU5s; expires=Fri, 08-Sep-2017 07:59:41 GMT; path=/; domain=.google.com.hk; HttpOnly',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'

}

url = 'https://www.google.com.hk/search?async=_id:rg_s,_pms:s&ei=WQvBWIiVDsyl0gTZ26WICA&yv=2&q=ginkgo+leaf&start=100&asearch=ichunk&newwindow=1&safe=strict&tbm=isch&vet=10ahUKEwjIpan7-cjSAhXMkpQKHdltCYEQuT0IHigB.WQvBWIiVDsyl0gTZ26WICA.i&ved=0ahUKEwjIpan7-cjSAhXMkpQKHdltCYEQuT0IHigB&ijn=1'
def get_images(url):
	wb_data = requests.get(url,headers=headers)
	data = wb_data.json()
	print type(data[1][1])
	#img_list = data['data']
	#for i in img_list:
	#	try:
	#		print (i['thumbURL'])
	#	except KeyError:
	#		pass
		#soup = BeautifulSoup(wb_data.text,'lxml')
		#print soup.prettify()
		#imges = soup.select('#imgid > div > ul > li > div > a > img')
		#print len(imges)
		#for i in imges:
		#	img_url.append(i)
		#return img_url

def download(_url,name):
	if(_url==None):
		pass
	result = urllib2.urlopen(_url)
	if(result.getcode()!=200):
		pass
	else:
		data=result.read()
		with open(name,"wb") as code:
			code.write(data)
			code.close

def get_pages(num):
	links = []
	for i in range(0,num,30):
		url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E9%93%B6%E6%9D%8F%E6%A0%91%E5%8F%B6%E5%9B%BE%E7%89%87&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%E9%93%B6%E6%9D%8F%E6%A0%91%E5%8F%B6%E5%9B%BE%E7%89%87&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn={}'.format(i)
		links.append(url)
	print links
	return links


get_images(url)
#link = []
#img_link = get_pages(300)
#for i in img_link:
#	get_images(i)
#print link

#for l in links:
#    get_images(l)
#count = 0
#for address in link:
#	if(address!=None):
#		pathName="E:\\leaf\\"+str(count+1)+".jpg"
#		download(address,pathName)
#		count = count + 1
#		print "downloading:",count
