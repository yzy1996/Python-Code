# 输出txt有多少行
# 使用with open的好处是：
with open(r'demo.txt', 'rt') as f:
    count=len(f.readlines())
    print(count)


# f = open(r'somefile.txt', 'rt')
# data = f.read()
# f.close()