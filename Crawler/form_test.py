import random

with open('ip.txt') as f:
    lines = (line.strip() for line in f)
    ip = list(lines)

with open('user_agent.txt') as f:
    lines = (line.strip() for line in f)
    user_agent = list(lines)

# user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36
# proxy-server=http://117.191.11.105:8080
headers = 'User-Agent=' + random.choice(user_agent)  # 随机选择浏览器标识
proxies = 'proxy-server=http://' + random.choice(ip)  # 代理ip
print(headers)
print(proxies)