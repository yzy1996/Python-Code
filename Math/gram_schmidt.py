# 施密特正交化 Gram-Schmidt

from numpy import *

def myGS(V):
    u = []
    E = []
    for i in range(len(V)):
        u.append(V[i])
        for j in range(i):
            u[i] -= (V[i] @ u[j]) / (u[j] @ u[j]) * (u[j])
        E.append(u[i] / linalg.norm(u[i]))
    return array(E)

# 输入矩阵  
V = array([[1., 0, -1, 4], [-1, 2, 2, -1], [2, 3, 1, -3]]).transpose()
print(V)

# 输出施密特正交化结果
E = myGS(V)
print(E)

# 验证是否为单位阵
print(E.transpose() @ E)