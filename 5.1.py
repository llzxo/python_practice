a = raw_input("input a string:")
length = len(a)
i=0
b=[]
while i<length:
    sss = a[i] + ":" + str(a.count(a[i]))
    i += 1

    if sss not in b:
        b.append(sss)

for j in b:
    print(j)

