from bs4 import BeautifulSoup
import requests
import urllib2

headers = {
	'Cookie':'BDqhfp=%E9%93%B6%E6%9D%8F%E6%A0%91%E5%8F%B6%E5%9B%BE%E7%89%87%26%260-10-1undefined%26%260%26%261; BAIDUID=29B8DCB5FA0769F905DBACB63E5B4757:FG=1; BIDUPSID=29B8DCB5FA0769F905DBACB63E5B4757; PSTM=1468308011; BDUSS=2Y4Smk2THdLaTFSeDNNYkw4ejdlYy1kS1lnajlMN3l6VWh3REFQZVJ3eHZ4ZVZZSVFBQUFBJCQAAAAAAAAAAAEAAAD22HwabGwwMzE3AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG84vlhvOL5YQ; MCITY=-75%3A; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=5; H_PS_PSSID=1465_21102_22037_22175_22159; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; indexPageSugList=%5B%22%E9%93%B6%E6%9D%8F%E6%A0%91%E5%8F%B6%E5%9B%BE%E7%89%87%22%5D; cleanHistoryStatus=0; userFrom=ala',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'

}

url2 = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E9%93%B6%E6%9D%8F%E5%8F%B6&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%E9%93%B6%E6%9D%8F%E5%8F%B6&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn=30'

url = 'https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%D2%F8%D0%D3%CA%F7%D2%B6%CD%BC%C6%AC&fr=ala&ori_query=%E9%93%B6%E6%9D%8F%E6%A0%91%E5%8F%B6%E5%9B%BE%E7%89%87&ala=0&alatpl=sp&pos=0&hs=2&xthttps=111111'
def get_images(url):
	wb_data = requests.get(url,headers=headers)
	data = wb_data.json()
	img_list = data['data']
	print type(img_list)
	#for i in img_list:
	#	try:
	#		link.append(i['thumbURL'])
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
		url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E9%93%B6%E6%9D%8F%E5%8F%B6&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%E9%93%B6%E6%9D%8F%E5%8F%B6&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn={}'.format(i)
		links.append(url)
	print links
	return links

get_images(url2)
#link = []
#img_link = get_pages(3000)
#for i in img_link:
#	get_images(i)
#print link

#for l in links:
#    get_images(l)
#count = 0
#for address in link:
#    if(address!=None):
#        pathName="E:\\leaf1\\"+str(count+1)+".jpg"
#        download(address,pathName)
#        count = count + 1
#        print "downloading:",count
