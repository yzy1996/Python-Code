# 测试网页爬虫的效果

import requests
import random
import time

with open('ip1.txt') as f:
    lines = (line.strip() for line in f)
    ip = list(lines)

url = 'http://httpbin.org/get'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}   

proxies = {'http':'http://117.191.11.105:8080'}

response = requests.get(url, headers=headers, proxies=proxies, timeout=5)

if response.status_code == 200:
    with open('html.txt', 'w', encoding='utf-8') as f:
        f.write(response.text)