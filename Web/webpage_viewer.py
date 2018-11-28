# -*- coding: utf-8 -*-

import urllib.request
import re

url = 'https://blog.csdn.net/yzy_1996/article/details/82916940'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

req = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(req)
page = response.read()

#利用正则表达式获取博客的访问量
view = re.findall('<span class="link_view".*?><a href=".*?" title="阅读次数">阅读</a>\((.*?)\)</span>', page,re.S)
#将结果输出 
print('访问量:%s' % (view.zfill(4)))