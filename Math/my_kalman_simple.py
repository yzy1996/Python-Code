'''本例说明
是Kalman滤波器的一种特殊情况，去掉了
设定真实值，按高斯分布，针对真实值随机生成【sz】个观测数据，然后进行卡尔曼滤波估计
'''

import numpy as np
import pylab

# 初始化参数
sz = 50  # 数据量

x = 0.1  # 真实值
z = np.random.normal(x, 0.1, size=sz)  # 观测值，服从高斯分布

Q = 1e-5  # 过程噪声
R = 1e-2  # 观测噪声

# 为变量分配空间
x_predict = np.zeros(sz)  # x的先验估计，也就是预测值
P_predict = np.zeros(sz)  # P的先验估计
x_update = np.zeros(sz)  # x的后验估计，也就是最终的估计量
P_update = np.zeros(sz)  # 协方差的后验估计
K = np.zeros(sz)  # 卡尔曼增益

# 赋初值
x_update[0] = 0.0
P_update[0] = 1.0

for k in range(1, sz):
    # 预测过程
    x_predict[k] = x_update[k - 1]
    P_predict[k] = P_update[k - 1] + Q

    # 更新过程
    K[k] = P_predict[k] / (P_predict[k] + R)
    x_update[k] = x_predict[k] + K[k] * (z[k] - x_predict[k])
    P_update[k] = (1 - K[k]) * P_predict[k]

pylab.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
pylab.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

pylab.figure()
pylab.plot(z, 'k+', label='观测值')  # 观测值
pylab.plot(x_update, 'b-', label='估计值')  # 估计值
pylab.axhline(x, color='g', label='真实值')  # 真实值
pylab.legend()
pylab.show()
