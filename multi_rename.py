import os

dir_name = os.getcwd()

file_list = os.listdir(dir_name)

for tmp in file_list:
    os.rename(tmp,tmp[5:])
