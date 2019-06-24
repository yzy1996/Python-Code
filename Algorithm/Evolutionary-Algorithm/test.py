# -*- coding: utf-8 -*-
import telnetlib
 
print('------------------------connect---------------------------')
# 连接Telnet服务器
try:
    tn = telnetlib.Telnet('5.190.166.242',port='80',timeout=10)
except:
    print('该代理IP  无效')
else:
    print('该代理IP  有效')
 
print('-------------------------end----------------------------')