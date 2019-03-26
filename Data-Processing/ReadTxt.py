# 读取txt数据并保存到数组
# txt数据类型为：每行带括号，用逗号隔开
# (id,length,speed,channel,from,to,isDuplex)
# (5000, 10, 5, 1, 1, 2, 1)
# (5001, 10, 5, 1, 2, 3, 1)
# (5002, 10, 5, 1, 3, 4, 1)
# (5003, 10, 5, 1, 4, 5, 1)
# (5004, 10, 5, 1, 5, 6, 1)

with open(r'car.txt') as f:
    next(f)  # 从txt的第二行开始了
    lines = f.readlines()
    print("数据有%d行" %(len(lines)))

    data = []                          
    for line in lines:              #把lines中的数据逐行读取出来
        temp1=line.strip('\n()').split(',')  # 去掉字符串首尾的分隔符
        data.append(temp)
