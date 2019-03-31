#加入需要的库
import csv
import os

#初始化工作
path='competition/train'
csvFile = open("2.csv", 'a',newline='')
writer = csv.writer(csvFile)	


#开始读写文件
files = os.listdir(path)
for file in files:
	command='tesseract.exe '+path+'/'+file+' output -l chi_sim+chi_sim1 --psm 7'
	os.popen(command).read()
	f = open('output.txt', 'r', encoding="utf8")    # 打开文件
	data=''
	for line in f.readlines():   
		data = data + line.strip()
	data = data.replace(' ', '')
	csvFile = open("2.csv", 'a', newline='')	
	add_info = [file, data]	
	writer.writerow(add_info)
	f.close()

csvFile.close()