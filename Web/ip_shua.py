from urllib import request
from random import randint

url = "http://xxxxx"

n = 1000

proxy = [{'https': '110.88.10.198'}, {'https': '182.88.117.118'}, {'https': '180.158.109.60'},
         {'https': '110.88.10.198'}, {'https': '122.235.184.109'}, {'https': '221.3.39.207'}]

for _ in range(n):
    proxy_support = request.ProxyHandler(proxy[randint(0, len(proxy)-1)])
    opener = request.build_opener(proxy_support)
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    request.install_opener(opener)
    response = request.urlopen(url)
    print((_ + 1) / n)