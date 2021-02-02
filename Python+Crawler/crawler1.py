# 1、爬虫起步

import urllib.request
import re 

response = urllib.request.urlopen('http://www.baidu.com')

content = response.read().decode('utf-8')

print(content)

