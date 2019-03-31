# 读取txt文件有多少行

with open(r'demo.txt', 'rt') as f:
    count=len(f.readlines())
    print("数据有%d行" %(count))