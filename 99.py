i=1
l1=[]
while i<10:
    l1.append(i)
    i += 1

def func():
    for i in l1:
        j = 1
        while j <= i:
            print ("%d*%d=%d"%(j,i,j*i)),
            j += 1
        print ""

func()
