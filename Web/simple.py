import requests
import time

url = ['https://blog.csdn.net/yzy_1996/article/details/85318705',
       'https://blog.csdn.net/yzy_1996/article/details/86992770',
       'https://blog.csdn.net/yzy_1996/article/details/87917772',
       'https://blog.csdn.net/yzy_1996/article/details/85318179',
       'https://blog.csdn.net/yzy_1996/article/details/88383365',
       'https://blog.csdn.net/yzy_1996/article/details/88896320',
       'https://crazyang.blog.csdn.net/article/details/88960229',
       'https://crazyang.blog.csdn.net/article/details/89139203',
       'https://blog.csdn.net/yzy_1996/article/details/89351413',
       'https://blog.csdn.net/yzy_1996/article/details/89308517',
       'https://blog.csdn.net/yzy_1996/article/details/89139203',
       'https://crazyang.blog.csdn.net/article/details/89321214',
       'https://blog.csdn.net/yzy_1996/article/details/89452063'
       ]

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}   

count = 0
countUrl = len(url)

# 访问次数设置
if count < 100:
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