import pymongo

client = pymongo.MongoClient('192.168.18.51',27017)
llzxo = client['llzxo']
sheet = llzxo['sheet']

'''
path = 'E:\pydownload\llzxo.txt'
with open(path,'r') as f:
	lines = f.readlines()
	for index,line in enumerate(lines):
		data = {
			'index':index,
			'line':line,
			'words':len(line.split())
		}
		sheet.insert_one(data)
'''


for item in sheet.find({'words':{'$lt':5}}):
	print (item)
