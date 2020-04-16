# 施密特正交化 Gram-Schmidt
# ！注意 例子中 输入向量为  (3, 1)T  (2, 2)T
# 输出向量为 (0.9., 0.3.)T (-0.3., 0.9.)T

import numpy as np

def myGS(V):
    u = V.copy().transpose()
    E = []
    for i in range(len(u)):
        for j in range(i):
            u[i] = (V[i] @ u[j]) / (u[j] @ u[j]) * (u[j])
        E.append(u[i] / np.linalg.norm(u[i]))
    return np.array(E)

if __name__ == "__main__":
    # 输入矩阵  
    # V = np.array([[3., 1.], [2., 2.]])
    V = np.array([[1., 0, -1, 4], [-1, 2, 2, -1], [2, 3, 1, -3]]).transpose()
    print(V)

    # # 输出施密特正交化结果
    E = myGS(V)
    print(E)
    
    # # 验证是否为单位阵
    print(E.transpose() @ E)