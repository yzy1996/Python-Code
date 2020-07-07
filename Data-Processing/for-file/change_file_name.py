import os

file_list = os.listdir()

for file in file_list:
    os.rename(file, file.replace(' ', '-'))
