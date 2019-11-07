'''本例说明
小车匀加速运动，对小车进行位移预测
'''

import numpy as np
import pylab

# 初始化参数
delta_t = 0.1
t = np.arange(0, 5, delta_t)  # 时间序列
N = len(t)  # 序列长度
sz = (2, N)  # 数据量
a = 10  # 真实加速度
x = 1 / 2 * a * t**2  # 真实位移
z = x + np.random.normal(0, 10, size=N)  # 观测值，在真实值上加入了白噪声，服从高斯分布

Q = [[0, 0], [0, 0.01]]
R = 10

A = np.array([[1, delta_t], [0, 1]])
B = np.array([1 / 2 * delta_t**2, delta_t])
H = np.array([1, 0])

# 分配空间
x_predict = np.zeros(sz)  # x的先验估计，也就是预测值
P_predict = np.zeros((2, 2))  # P的先验估计
x_update = np.zeros(sz)  # x的后验估计，也就是最终的估计量
P_update = np.zeros((2, 2))  # 协方差的后验估计
K = np.zeros(sz)  # 卡尔曼增益
I = np.eye(2)

for k in range(1, N):
    # 预测过程
    x_predict[:, k] = A.dot(x_update[:, k - 1]) + a * B
    P_predict = A.dot(P_update).dot(A.T) + Q

    # 更新过程
    K[:, k] = P_predict.dot(H.T) / (H.dot(P_predict).dot(H.T) + R)
    x_update[:, k] = x_predict[:, k] + K[:, k].dot(
        (z[k] - H.dot(x_predict[:, k])))
    P_update = (I - K[:, k].dot(H)).dot(P_predict)

pylab.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
pylab.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

pylab.figure()
pylab.plot(z, color='g', linestyle='--', label='观测值')  # 观测值
pylab.plot(x_update[0], color='r', label='估计值')  # 估计值
pylab.plot(x, linestyle=':', label='真实值')  # 真实值
pylab.xlabel('时间/s')
pylab.ylabel('位移/m')
pylab.legend()
pylab.show()