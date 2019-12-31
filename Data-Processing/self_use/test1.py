import csv
import os, sys

path ='11'
dirs = os.listdir(path)
dirs.sort(key=len)

# for file in dirs:
#     filepath = path + '/' + file
    # with open(filepath, 'w') as f:
    #     lines = (line.strip() for line in f)  # 得到一个迭代器
    #     for line in lines:
    #         line_new = line.replace(':',',')
    #         f.write(line_new)

    # f1 = open(filepath,'r+')
    # infos = f1.readlines()
    # f1.seek(0,0)
    # for line in infos:
    #     line_new = line.replace(':',',')
    #     f1.write(line_new)
    # f1.close()

column1 = [0]*1008
for file in dirs:
    filepath = path + '/' + file
    with open(filepath, 'r') as csvfile:
        reader = csv.reader(csvfile)      
        column = [row[32] for row in reader]
        column = [float(i) for i in column]
        for i in range(len(column)):
            column1[i] += column[i]

with open('222.txt', 'w') as f:
    for ip in column1:
	    f.write(str(ip))
	    f.write('\n')

# print(column1)

