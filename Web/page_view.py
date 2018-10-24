# 该程序实现刷CSDN网页访问量，当访问被拒绝或者遇到其他异常时会自动重启，无限刷
# 经过测试发现大概间隔70秒访问一下，访问量才会增加1
# 只需要修改或者添加url的链接就可以了

from urllib import request
import time
import os, sys

url = ['https://blog.csdn.net/yzy_1996/article/details/82916940']

countUrl = len(url)
count = 0
count1 = 0

while True:  #让程序一直执行
    if count1 < 1000:
        try:  #正常运行
            count = count + 1
            print(count, 'times')  #监视程序是否在正常运行，输出运行了多少次
            for i in range(countUrl):  #遍历所有url
                request.urlopen(url[i])  #访问网页
            time.sleep(70)  #间隔执行

        except Exception:  #出现异常
            print('Retry')
            count1 = count1 + 1
            time.sleep(70)  #间隔执行
