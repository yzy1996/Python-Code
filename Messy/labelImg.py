# -*- coding: utf-8 -*-
import os
import sys
#import natsort
import xml.etree.ElementTree as ET
file_dir='D:\BD-label'

def file_name(file_dir):
    L=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.xml':
                L.append(os.path.join(root, file))
    return L

if  __name__=='__main__':
    Num=file_name(file_dir)
    Num.sort()
    for i in range(241,len(Num)-1):   #每个单独的文件
        print Num[i]
        name=Num[i].split('\\')[2]
        print name
        tree = ET.parse(Num[i])
        root = tree.getroot()
        object = root.findall("object")
        count=0
        for tmp in object:     #every object
            count=count+1
            a=tmp
            d=ET.SubElement(a, 'index')
            d.text=str(count)
            d.tail="\n\t\t"
            #print(a.find('name').text)
            print("print No.%d     %s 's father index.End with 0\n"%(count,a.find('name').text))

            b = ET.SubElement(a, 'father')
            b.text="\n\t\t\t"
            b.tail="\n\t\t"
            count_father=0
            while(True):
                count_father = count_father+1
                insert_num=input()
                if(insert_num==0):
                    break
                c=ET.SubElement(b,'num'+str(count_father))
                c.text=str(insert_num)
                c.tail = "\n\t\t\t"
            print("print No.%d     %s's child num. End with 0\n" % (count,a.find('name').text))
            a = tmp
            b = ET.SubElement(a, 'child')
            b.text = "\n\t\t\t"
            b.tail = "\n\t"
            count_child=0
            while (True):
                count_child=count_child+1
                insert_num = input()
                if (insert_num == 0):
                    break
                c = ET.SubElement(b, 'num'+str(count_child))
                c.text = str(insert_num)
                c.tail = "\n\t\t\t"
            tree.write(name)
