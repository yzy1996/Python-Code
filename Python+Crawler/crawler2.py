# 2、爬虫进阶

import os
from urllib import parse, request


def require_env(name):
    value = os.getenv(name)
    if value:
        return value
    raise RuntimeError(f"Missing environment variable: {name}")


url = 'https://biihu.cc//account/ajax/login_process/'
headers = {'User-Agent':' Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
payload = {
    'return_url':'https://biihu.cc/',
    'user_name': require_env('BIIHU_USERNAME'),
    'password': require_env('BIIHU_PASSWORD'),
    '_post_type':'ajax',
}
data = bytes(parse.urlencode(payload), 'utf-8')

req = request.Request(url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))