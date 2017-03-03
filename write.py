f=open('123.txt','r')
#f.write('hello llzxo')
content = f.read(6)
#print (type(content))
#print content

contents = f.readline()
print(type(contents))
f.close()
