# 使用requests库

import requests

url = 'http://www.baidu.com'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

response = requests.get(url, headers=headers)

content = response.content.decode('utf-8')

print(content)

