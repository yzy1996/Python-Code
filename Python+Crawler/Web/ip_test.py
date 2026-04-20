import socket
 
print('------------------------connect---------------------------')
# 探测 TCP 连接可用性
try:
    with socket.create_connection(('111.20.226.13', 9808), timeout=10):
        pass
except OSError:
    print('该代理IP  无效')
else:
    print('该代理IP  有效')
 
print('-------------------------end----------------------------')