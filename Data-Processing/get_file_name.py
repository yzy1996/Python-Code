# 获取文件名，且不要后缀名

import os

path = r'demo.txt'
name = os.path.splitext(os.path.basename(path))[0]  
print(name)