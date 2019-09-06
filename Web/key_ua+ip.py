import requests
import random
import time

url = 'http://www.baidu.com'

with open('ip.txt') as f:
    lines = (line.strip() for line in f)
    ip = list(lines)

with open('user_agent.txt') as f:
    lines = (line.strip() for line in f)
    user_agent = list(lines)
    
count = 0
count1 = 0

while True: 
    # 访问次数设置
    if count < 1000:

        headers = {'User-Agent': random.choice(user_agent)}  # 随机选择浏览器标识

        payload = {'key': '如吉生物'}  # 检索关键词

        proxies = {'http': 'http://' + random.choice(ip)}  # 代理ip

        try:  # 正常运行
            response = requests.get(url, params=payload, headers=headers, proxies=proxies, timeout=5)
            if response.status_code == 200:
                count = count + 1
                print(count, 'times')
            # time.sleep(60)

        except Exception:  # 异常
            print('Retry')
            # time.sleep(60)
    else:
        break