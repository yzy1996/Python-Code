# ADAM
# 以 y=x1+2*x2为例
import math
import numpy as np


def adam():
    # 训练集，每个样本有三个分量
    x = np.array([(1, 1), (1, 2), (2, 2), (3, 1), (1, 3), (2, 4), (2, 3), (3,
                                                                           3)])
    y = np.array([3, 5, 6, 5, 7, 10, 8, 9])

    # 初始化
    m, dim = x.shape
    theta = np.zeros(dim)  # 参数
    alpha = 0.01  # 学习率
    momentum = 0.1  # 冲量
    threshold = 0.0001  # 停止迭代的错误阈值
    iterations = 3000  # 迭代次数
    error = 0  # 初始错误为0

    b1 = 0.9  # 算法作者建议的默认值
    b2 = 0.999  # 算法作者建议的默认值
    e = 0.00000001  #算法作者建议的默认值
    mt = np.zeros(dim)
    vt = np.zeros(dim)

    for i in range(iterations):
        j = i % m
        error = 1 / (2 * m) * np.dot((np.dot(x, theta) - y).T,
                                     (np.dot(x, theta) - y))
        if abs(error) <= threshold:
            break

        gradient = x[j] * (np.dot(x[j], theta) - y[j])
        mt = b1 * mt + (1 - b1) * gradient
        vt = b2 * vt + (1 - b2) * (gradient**2)
        mtt = mt / (1 - (b1**(i + 1)))
        vtt = vt / (1 - (b2**(i + 1)))
        vtt_sqrt = np.array([math.sqrt(vtt[0]),
                             math.sqrt(vtt[1])])  # 因为只能对标量进行开方
        theta = theta - alpha * mtt / (vtt_sqrt + e)

    print('迭代次数：%d' % (i + 1), 'theta：', theta, 'error：%f' % error)


if __name__ == '__main__':
    adam()