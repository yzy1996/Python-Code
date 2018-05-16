import os
import csv
import shutil

#添加地址路径等信息
path='competition/test'
file='test.png'

#执行tesseract进行OCR处理
def do_tesseract():
	command='tesseract.exe '+path+'/'+file+' output -l chi_sim'
	os.popen(command).read()

#读取txt，读取每一行然后组成一整个字符串
def read_txt():
	f = open('output.txt', 'r',encoding="utf8")    # 打开文件
	data=''
	for line in f.readlines():   
		data = data + line.strip()
	data = data.replace(' ', '')
	print(data)
	f.close()

#在csv文件末尾添加内容	
def add2csv():
	f = open('output.txt', 'r',encoding="utf8")    # 打开文件
	data=''
	for line in f.readlines():   
		data = data + line.strip()
	data = data.replace(' ', '')
	csvFile = open("2.csv", 'a', newline='')	
	writer = csv.writer(csvFile)
	add_info = ['A9900.png', data]	
	writer.writerow(add_info)

#去掉txt末尾的内容	
def cuttxtlast():
	f = open('output.txt', 'r+', encoding="utf8")    # 打开文件
	data = f.readlines()                 # 读取文件内容
	f.close()
	w = open('output.txt', 'w', encoding="utf8")    # 打开文件
	w.writelines(data[:-1])
	print(data)
	w.close()

#查找csv文件中第二列为空的项	
def findcsv():
	csvFile = open("test3.csv", "r", encoding="utf8")
	reader = csv.reader(csvFile)

	for item in reader:
		if reader.line_num == 1:            #去掉第一行
			continue 					    #在for循环中起作用
		if item[1]=='':
			# print(item[0])
			shutil.copy2(path+'/'+item[0], './111')

#复制文件			
def copyy():
	aaa='A9900.png'
	shutil.copy2(path+'/'+aaa, './111')

#替换csv文件中的内容
def replace():
	csvFile1 = open("111.csv", "r", encoding="utf8")
	reader1 = csv.reader(csvFile1)
	csvFile2 = open("222.csv", "r", encoding="utf8")
	reader2 = csv.reader(csvFile2)
	csvFile3 = open("333.csv", 'a', newline='')
	writer = csv.writer(csvFile3)
	for item1 in reader1:
		if item1[1]=='':
			for item2 in reader2:
				if item1[0]==item2[0]:
					add_info = [item1[0], item2[1]]	
					writer.writerow(add_info)
					break
		else:
			add_info = [item1[0], item1[1]]	
			writer.writerow(add_info)
	csvFile1.close()
	csvFile2.close()
	csvFile3.close()

#主程序执行吧	
replace()