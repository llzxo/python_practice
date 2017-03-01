def welcome():
    print("*" * 20)
    print("press 1 to insert")
    print("press 2 to delete")
    print("press 3 to update")
    print("press 4 to search")
    print("press 5 to exit")
    print("*" * 20)

def usr_insert():
    name_input = raw_input("input name:")
    age_input = input("input age:")
    tmp={}
    tmp['name'] = name_input
    tmp['age'] = age_input
    tmp['id'] = len(usr_list)
    usr_list.append(tmp)
    print ""

def usr_delete():
    print_list()
    id_input = input("input student number to delete(digit):")
    if id_input >= 0 and id_input < len(usr_list):
        confirm = raw_input("confirm to delete %d?(yes/no)"%id_input)
        confirm = confirm.lower()
        if confirm == "yes":
            usr_list.pop(id_input)
    print_list()
    print ""

def usr_update():
    print_list()
    id_input = input("input student number to update(digit):")
    if id_input >= 0 and id_input < len(usr_list):
        confirm = raw_input("confirm to update %d?(yes/no)"%id_input)
        confirm = confirm.lower()
        if confirm == "yes":
            name_input = raw_input("input name:")
            age_input = input("input age:")
            tmp={}
            tmp['name'] = name_input
            tmp['age'] = age_input
            tmp['id'] = id_input
            usr_list[id_input] = tmp
    print ""


def usr_search():
     name_input = raw_input("input name to search:")
     list_len = len(usr_list)
     x = 0
     for tmp in usr_list:
         if tmp['name'] == name_input:
             print("student find:")
             print("name:%s,age:%d,id:%d"%(usr_list[x]['name'],usr_list[x]['age'],usr_list[x]['id']))

   # while x < list_len :
   #     if name_input == usr_list[x]['name']:
   #         print("student find:")
   #         print("name:%s,age:%d,id:%d"%(usr_list[x]['name'],usr_list[x]['age'],usr_list[x]['id']))
   #         break
   #     x += 1
   # if x == list_len:
   #     print("not find")
   # print ""

def print_list():
    for i in usr_list:
         print i

usr_list=[]
while True:
    welcome()
    usrinput = raw_input("input ")
    usrinput = int(usrinput)

    if usrinput == 1 :
        usr_insert()
    elif usrinput == 2 :
        usr_delete()
    elif usrinput == 3 :
        usr_update()
    elif usrinput ==4 :
        usr_search()
    elif usrinput == 5 :
        confirm = raw_input("exit?(yes/no)")
        if confirm == "yes" or confirm == "YES":
            break
    else:
        print("please input again:")

print_list()
