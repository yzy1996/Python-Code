import urllib.request
import re
f = open('ip.txt', 'a')
for i in range(10):
    url_ip = 'http://183.129.244.16:88/open?user_name=lhq_1127105224_8841e&timestamp=1542872066&md5=902b0c298e4d1fb3acfdba5a5ce2b664&pattern=txt&number=200'
    response = urllib.request.urlopen(url_ip)
    ip=response.read()
    ip=ip.decode("utf-8")
    ip = re.split('\n', ip)
    ip = '\n'.join(ip[4:204])
    ip = '\n' + ip  
    f.write(ip)
f.close()