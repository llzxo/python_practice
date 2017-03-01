def prime(n):
    if n==1:
        return True#False
    elif n==2:
        return False#True
    else:
        i = 2
        while i < n:
            if n%i == 0 :
                return False#True
            i += 1
            if i == n:
                return True#False
j = 1
num_list = []
while(j<=100):
    num_list.append(j)
    j+=1


new_list = filter(prime,num_list)

for i in new_list:
    print i
