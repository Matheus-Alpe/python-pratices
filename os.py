# import os
# files = os.listdir('.')

# for file in files:
#     print(file)

from os import listdir
from os.path import isfile, join, splitext

my_path = "./os_test/"
onlyfiles = [file for file in listdir(my_path) if isfile(join(my_path, file)) and splitext(file)[1] == '']
onlyfiles = sorted(onlyfiles)

print(onlyfiles)

for nameFile in onlyfiles:
    with open("./os_test/"+nameFile, "r") as file:
        for line in file:
            print(nameFile, '->', line)
    
    file.close()