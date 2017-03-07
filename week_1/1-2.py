from bs4 import BeautifulSoup
with open('C:\Users\llzxo\Desktop\Plan-for-combating-master\week1\\1_2\\1_2answer_of_homework\\1_2_homework_required\index.html','r') as wb_date:
    Soup = BeautifulSoup(wb_date,'lxml')
    images = Soup.select('body > div > div > div > div > div > div > img')
    prices = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right')
    names = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4 > a')
    rate_nums = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p.pull-right')
    rates = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p:nth-of-type(2)')
for i in rates:
    print type(i)

for image,price,name,rate_num,rate in zip(images,prices,names,rate_nums,rates):
    data = {
        'image': image.get('src'),
        'price':price.get_text(),
        'name':name.get_text(),
        'rate_num':rate_num.get_text(),
        'rate:':len(rate.find_all("span",class_="glyphicon glyphicon-star"))
    }
    print (data)



