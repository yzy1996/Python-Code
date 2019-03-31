# -*- coding: utf-8 -*-
import os
import csv
import shutil
from PIL import Image
import cv2

#添加地址路径等信息
path='competition/test_now'
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
	csvFile1 = open("test.csv", "r", encoding="utf8")                   #地址文件名需要修改
	reader = csv.reader(csvFile1)
	# csvFile2 = open("3.csv", 'a', newline='')	                           #地址文件名需要修改
	# writer = csv.writer(csvFile2)
	
	for item in reader:
		if reader.line_num == 1:            #去掉第一行
			continue 					    #在for循环中起作用
		if item[1]=='':
			# print(item[0])
			shutil.copy2(path+'/'+item[0], './copy')                       #目标地址文件需要修改
			
			#这是在一个新的csv中预留空的第二行
			# add_info = [item[0], '']	      
			# writer.writerow(add_info)	
			
	csvFile1.close()
	
#复制文件			
def copyy():
	aaa='A9900.png'
	shutil.copy2(path+'/'+aaa, './111')

#替换csv文件中的内容
#111是原始待补充的
#222是补充的
#333是补充完的
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
					add_info = [item1[0], "".join(item2[1:])]	
					writer.writerow(add_info)
					break
		else:	
			writer.writerow(item1)
	csvFile1.close()
	csvFile2.close()
	csvFile3.close()
	
#测试参数
def testprama():
	files = ''
	csvFile = open("test_dia.csv", 'a',newline='')
	writer = csv.writer(csvFile)
	rrange = [6,7,8,10,13]
	for psm in range:
		command='tesseract.exe '+file+' output -l chi_sim+chi_sim1 --psm '+psm
		os.popen(command).read()
		f = open('output.txt', 'r', encoding="utf8")    # 打开文件
		data=''
		for line in f.readlines():   
			data = data + line.strip()
		data = data.replace(' ', '')
		add_info = [file, data]	
		writer.writerow(add_info)
		f.close()
	csvFile.close()
	
#自由测试
def freetest():	
	pic = cv2.imread('A14136.png')
	pic = cv2.resize(pic, (400, 400), interpolation=cv2.INTER_CUBIC)
	cv2.imshow('', pic)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def changecsv():
	csvFile = open("111.csv", "r", encoding="utf8")
	reader = csv.reader(csvFile)
	csvFile3 = open("333.csv", 'a', newline='')
	writer = csv.writer(csvFile3)
	for item in reader:
		writer.writerow(item)
	csvFile.close()

#将大批量的图片分成自定义的一小份一小份，然后可以多人同时训练
def divPicture():
	n=2             ###设定每一份包含多少张图片
	pathcount=0     ###设定文件夹的序号
	count=0
	files = os.listdir('111')      ###path需要修改
    
	os.makedirs(str(pathcount))            #makedirs 创建文件时如果路径不存在会创建这个路径  
	for file in files:
		if count<n:			
			count=count+1
		else:
			count=1
			pathcount=pathcount+1
			os.makedirs(str(pathcount))            #makedirs 创建文件时如果路径不存在会创建这个路径  
			
		shutil.copy2('111/'+file, './'+str(pathcount))	
		
#读取图像的尺寸大小（像素值）
def readpixel():
	img = cv2.imread("3.png")
	size = img.shape
	print(size)

def resultPlus():
	csvFile1 = open("1.csv", "r", encoding="utf8")
	reader1 = csv.reader(csvFile1)
	csvFile2 = open("2.csv", "r", encoding="utf8")
	reader2 = csv.reader(csvFile2)
	csvFile3 = open("3.csv", 'a', newline='')
	writer = csv.writer(csvFile3)
	for item1 in reader1:
		for item2 in reader2:
			if item1[0]==item2[0]:
				add_info = [item1[0], "".join(item1[1:])+"".join(item2[1:])]	
				writer.writerow(add_info)
				break
	csvFile1.close()
	csvFile2.close()
	csvFile3.close()

#执行图片的文字块抠取程序
#是调用的另一个py程序
def picture1word():
files = os.listdir(path)
	for file in files:
		command='python crop_morphology.py test_f/'+file
		os.popen(command)	
		
#主程序执行吧	
resultPlus()