fileName = raw_input("input filename to copy:")

new_fileName = fileName[0:fileName.rfind(".")] +"(copy)" + fileName[fileName.rfind("."):]

f1 = open(fileName,'r')
content = f1.readline()
f2 = open(new_fileName,'w')
while(len(content)):
    f2.write(content)
    content = f1.readline()

f1.close()
f2.close()

