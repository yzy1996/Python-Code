'''
    在这里将用代码实现一些数学中常用的概念，方便理解
    1、均方误差
'''
import numpy as np
import matplotlib.pyplot as plt

# 生成一组随机数
x1 = np.random.rand(10) 
x2 = np.random.randn(100) # 标准正态分布
x3 = np.random.randint(1, 10, 10) # 1-10的整数
x4 = np.random.normal(size=10)

# 生成一组真实值和预测值
target = [1, 2, 3, 4, 5, 6]
prediction = [1, 1, 2, 4, 4, 7]


## 对单组数据而言
# 计算均值
# mean = np.mean(target)
# print('均值:', mean)

# # 计算方差
# var = np.var(target)
# print('方差：', var)

## 对两组数据而言
# 计算误差
error = []
for i in range(len(target)):
    error.append(target[i] - prediction[i])

squaredError = []
for val in error:
    squaredError.append(val^2)

print('MSE:', sum(squaredError)/len(squaredError)) 

# 计算标准差
std = np.std(target)
print(std)
# 画出随机数的图像
# plt.figure(1)
# plt.plot(x4)
# # plt.figure(2)
# # plt.hist(x4, 100)
# plt.show()

# 1、均方误差(MSE)
# print("MSE = ", sum(squaredError) / len(squaredError))
