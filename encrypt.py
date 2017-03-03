def encrypt():
    file_name = raw_input("input file name to encrypt:")
    pass_word = input("input your password")

    num = file_name.rfind(".")

    f1 = open(file_name,'r')
    f2 = open(file_name[0:num] + "encrypt" + file_name[num:],'w')

    content = f1.read(1)
    while len(content) > 0:
        newcontent = chr(ord(content) + pass_word)
        f2.write(newcontent)
        content = f1.read(1)

    f1.close()
    f2.close()

def decode():
    file_name = raw_input("input file name to decode:")
    pass_word = input("input your password")

    num = file_name.rfind(".")

    f1 = open(file_name,'r')
    f2 = open(file_name[0:num-7] + "decode" + file_name[num:],'w')

    content = f1.read(1)
    while len(content) > 0:
        newcontent = chr(ord(content) - pass_word)
        f2.write(newcontent)
        content = f1.read(1)

    f1.close()
    f2.close()


def welcome():
    print("*" * 20)
    print("press 1 to encrypt a file:")
    print("press 2 to encode a file")
    print("press 3 to exit")
    print("*" * 20)


#l = [1,2,3]
#j = 0
#for i in l:
#    l[j] = i + 1
#    j+=1
#for i in l:
#    print i

while True:
    welcome()
    usr_input = input("")
    if usr_input == 1:
        encrypt()
    elif usr_input == 2:
        decode()
    elif usr_input == 3:
        break
    else:
        print("please input 1/2/3")
