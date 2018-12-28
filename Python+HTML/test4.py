# 读取生成的input.txt内容
f1 = open('input.txt') # 读取的数据类型为str
number1 = int(f1.read())

# 执行你要执行的程序（例子为计算平方）
number2 = number1 * number1

# 把运行的结果写入result.txt中
f2 = open('result.txt', 'w')
f2.write((str(number2)))

f1.close()
f2.close()