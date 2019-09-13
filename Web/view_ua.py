# 该程序实现刷CSDN网页访问量，当访问被拒绝或者遇到其他异常时会自动重启，无限刷
# 经过测试发现大概间隔70秒访问一下，访问量才会增加1
# 只需要修改或者添加url的链接就可以了
 
import requests
import time

url = ['https://crazyang.blog.csdn.net/article/details/97399885',
       'https://blog.csdn.net/yzy_1996/article/details/96448348',
       'https://blog.csdn.net/yzy_1996/article/details/90201584',
       'https://blog.csdn.net/yzy_1996/article/details/89818995',
       'https://blog.csdn.net/yzy_1996/article/details/89815744',
       'https://blog.csdn.net/yzy_1996/article/details/89815633',
       'https://blog.csdn.net/yzy_1996/article/details/89738312',
       'https://blog.csdn.net/yzy_1996/article/details/89482718',
       'https://crazyang.blog.csdn.net/article/details/87918378',
       'https://blog.csdn.net/yzy_1996/article/details/84504723',
       'https://blog.csdn.net/yzy_1996/article/details/83756198',
       'https://blog.csdn.net/yzy_1996/article/details/82945869',
       'https://blog.csdn.net/yzy_1996/article/details/82223241',
       'https://blog.csdn.net/yzy_1996/article/details/81909444',
       'https://blog.csdn.net/yzy_1996/article/details/81230126',
       'https://blog.csdn.net/yzy_1996/article/details/81230104',
       'https://blog.csdn.net/yzy_1996/article/details/100540556'     
       ]

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}   
 
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
        time.sleep(70)

    except Exception:  # 异常
        print('Failed and Retry')
        time.sleep(60)