import urllib.request
import re
import time
f = open('ip.txt', 'a')
for i in range(100):
    url_ip = 'http://webapi.http.zhimacangku.com/getip?num=20&type=1&pro=&city=0&yys=0&port=1&pack=35845&ts=0&ys=0&cs=0&lb=4&sb=0&pb=4&mr=2&regions='
    response = urllib.request.urlopen(url_ip)
    ip=response.read()
    ip=ip.decode("utf-8")
    print(ip)
    # ip = re.split('\n', ip)
    # ip = '\n'.join(ip)
    # # ip = '\n' + ip  
    f.write(ip)
    time.sleep(2)
f.close()
