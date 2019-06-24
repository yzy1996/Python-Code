import telnetlib
 
print('------------------------connect---------------------------')
# 连接Telnet服务器
try:
    tn = telnetlib.Telnet('111.20.226.13',port='9808',timeout=10)
except:
    print('该代理IP  无效')
else:
    print('该代理IP  有效')
 
print('-------------------------end----------------------------')