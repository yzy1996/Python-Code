import numpy as np

'''
list列表 [1, 2]
np.array数组 np.array([1, 2])
np.mat矩阵 np.mat([1, 2])
数组矩阵两者可以互相转换

!!!不要用列表来进行运算，下面只说数组和矩阵
'''

# 1-D
a = np.array([[1, 2], [3, 4]])
b = np.array([[2, 4], [1, 3]])

print(a.shape) # [3 8] 点乘
print(a.T @ b) # 11 乘
print(a.dot(b)) # 11 乘

