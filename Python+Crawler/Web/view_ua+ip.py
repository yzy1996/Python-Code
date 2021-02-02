import requests
import random
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
       'https://blog.csdn.net/yzy_1996/article/details/89452063',
       'https://crazyang.blog.csdn.net/article/details/89556049',
       'https://crazyang.blog.csdn.net/article/details/89527834',
       'https://crazyang.blog.csdn.net/article/details/89452063',
       'https://crazyang.blog.csdn.net/article/details/89164827',
       'https://blog.csdn.net/yzy_1996/article/details/89519702',
       'https://crazyang.blog.csdn.net/article/details/83756357'
       ]

with open('ip1.txt') as f:
    lines = (line.strip() for line in f)
    ip = list(lines)

with open('user_agent.txt') as f:
    lines = (line.strip() for line in f)
    user_agent = list(lines)
    
count = 0
countUrl = len(url)

# 访问次数设置
for i in range(1000):

    headers = {'User-Agent': random.choice(user_agent)}  # 随机选择浏览器标识

    proxies = {'http': 'http://' + random.choice(ip)}  # 代理ip
    
    print(proxies)
    try:  # 正常运行
        for i in range(countUrl):
            response = requests.get(url[i], headers=headers, proxies=proxies)
            if response.status_code == 200:
                count = count + 1
                print('Success', count, 'times')
                time.sleep(2)
        time.sleep(70)

    except Exception:  # 异常
        print('Retry')
        time.sleep(60)