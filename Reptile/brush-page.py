from urllib import request
import time

count = 0

url = ['https://blog.csdn.net/yzy_1996/article/details/81939610',
        'https://blog.csdn.net/yzy_1996/article/details/81909444',
        'https://blog.csdn.net/yzy_1996/article/details/81235807',
        'https://blog.csdn.net/yzy_1996/article/details/81230126',
        'https://blog.csdn.net/yzy_1996/article/details/81230104',
        'https://blog.csdn.net/yzy_1996/article/details/81135988',
        'https://blog.csdn.net/yzy_1996/article/details/81064140',
        'https://blog.csdn.net/yzy_1996/article/details/80797371',
        'https://blog.csdn.net/yzy_1996/article/details/80223053',
        'https://blog.csdn.net/yzy_1996/article/details/79611646']

while True:     #让程序一直执行
	count = count + 1
	print(count)			  #监视程序是否在正常运行
	for i in range(10):   #要刷多少个网页
		request.urlopen(url[i])    #访问网页
	
	if i == 9:
		i = 0
	time.sleep(70)   #间隔60秒执行一次