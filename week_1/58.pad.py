from bs4 import BeautifulSoup
import requests

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Referer':'http://bj.58.com/pingbandiannao/26062681492781x.shtml?adtype=1&entinfo=26062681492781_0&psid=118298279195149411398908275',
    'Cookie':'id58=c5/nn1gqubrCLkOvD8XYAg==; ipcity=cd%7C%u6210%u90FD%7C0; als=0; commonTopbar_myfeet_tooltip=end; bj58_id58s="Mzg9dGhoVVhLdEI5MTgyMw=="; sessionid=cd18247f-7739-459b-a272-6c1645687bda; myfeet_tooltip=end; bangbigtip2=1; city=cd; commontopbar_city=102%7C%u6210%u90FD%7Ccd; 58home=bj; 58tj_uuid=eb86b0a0-ded1-4db4-ac25-ae77aaa9bec2; new_session=0; new_uv=2; utm_source=; spm=; init_refer=http%253A%252F%252Fcd.58.com%252Fpbdn%252F%253Fkey%253D%2525E5%2525B9%2525B3%2525E6%25259D%2525BF%2525E7%252594%2525B5%2525E8%252584%252591%2526cmcskey%253D%2525E5%2525B9%2525B3%2525E6%25259D%2525BF%2525E7%252594%2525B5%2525E8%252584%252591%2526jump%253D3%2526searchtype%253D1%2526sourcetype%253D5; final_history=26062681492781%2C24727016501813%2C26088204291258%2C23434142745120%2C28701797893709; bj58_new_session=0; bj58_init_refer="http://cd.58.com/pbdn/?key=%E5%B9%B3%E6%9D%BF%E7%94%B5%E8%84%91&cmcskey=%E5%B9%B3%E6%9D%BF%E7%94%B5%E8%84%91&jump=3&searchtype=1&sourcetype=5"; bj58_new_uv=2'
}

def get_url():
    url_list = []
    url = 'http://cd.58.com/pingbandiannao/1/'
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    link = soup.select('a.t')
    for l in link:
        url_list.append(l.get('href'))
    return url_list

def get_views_count(url):
    id = url[url.rfind('=')+1:url.rfind('_')]
    api = 'http://jst1.58.com/counter?infoid={}'.format(id)
    js = requests.get(api,headers=headers)
    views = js.text
    return views
    print api
    print id
    print views

def get_attractions(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    title = soup.select('#content > div.person_add_top.no_ident_top > div.per_ad_left > div.col_sub.mainTitle > h1')[0].get_text()
    price = soup.select('span.price.c_f50')[0].get_text()
    date =  soup.select('li.time')[0].get_text()
    for r in soup.select('span.c_25d > a'):
        region.append(r.get_text())
    new = soup.select('#content > div.person_add_top.no_ident_top > div.per_ad_left > div.col_sub.sumary > ul > li:nth-of-type(2) > div.su_con > span')[0].get_text().strip()
    count = get_views_count(url).split('=')[-1]
    data={
        'title':title,
        'price':price,
        'date':date,
        'region':region,
        'new':new,
        'count':count
    }
    f = open("E:\pydownload\\58.txt",'w')
    for d in data:
        f.write(d)
    print data


'''def get_count(url):
    wb_data = requests.get
    return count
'''

region = []
links = get_url()
for i in get_url():
    get_attractions(i)
