# 该程序实现刷CSDN网页访问量，当访问被拒绝或者遇到其他异常时会自动重启，无限刷
# 经过测试发现大概间隔70秒访问一下，访问量才会增加1
# 只需要修改或者添加url的链接就可以了
 
import requests
import time

url = ['https://blog.csdn.net/yzy_1996/article/details/101563858',
       'https://blog.csdn.net/yzy_1996/article/details/102665398']

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}   
 
count = 0
countUrl = len(url) 

# 访问次数设置
while count < 10000:
    try:  # 正常运行
        for i in range(countUrl):
            response = requests.get(url[i], headers=headers)
            if response.status_code == 200:
                count = count + 1
                print('Success ' + str(count), 'times')
        time.sleep(100)

    except Exception:  # 异常
        print('Failed and Retry')
        time.sleep(1)