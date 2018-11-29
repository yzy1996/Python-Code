# 批量梯度下降BGD
# 拟合函数为：y = theta * x
# 代价函数为：J = 1 / (2 * m) * ((theta * x) - y) * ((theta * x) - y).T;
# 梯度迭代为: theta = theta - alpha / m * (x * (theta * x - y).T);
import numpy as np


# 1、单元数据程序
# 以 y=x为例，所以正确的结果应该趋近于theta = 1
def bgd_single():
    # 训练集, 单样本
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    y = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    # 初始化
    m = len(y)
    theta = 0  # 参数
    alpha = 0.01  # 学习率
    threshold = 0.0001  # 停止迭代的错误阈值
    iterations = 1500  # 迭代次数
    error = 0  # 初始错误为0

    # 迭代开始
    for i in range(iterations):
        error = 1 / (2 * m) * np.dot(((theta * x) - y).T, ((theta * x) - y))
        # 迭代停止
        if abs(error) <= threshold:
            break

        theta -= alpha / m * (np.dot(x.T, (theta * x - y)))

    print('单变量：', '迭代次数： %d' % (i + 1), 'theta： %f' % theta,
          'error1： %f' % error)


# 2、多元数据程序
# 以 y=x1+2*x2为例，所以正确的结果应该趋近于theta = [1，2]


def bgd_multi():
    # 训练集，每个样本有2个分量
    x = np.array([(1, 1), (1, 2), (2, 2), (3, 1), (1, 3), (2, 4), (2, 3), (3,
                                                                           3)])
    y = np.array([3, 5, 6, 5, 7, 10, 8, 9])

    # 初始化
    m, dim = x.shape
    theta = np.zeros(dim)  # 参数
    alpha = 0.01  # 学习率
    threshold = 0.0001  # 停止迭代的错误阈值
    iterations = 1500  # 迭代次数
    error = 0  # 初始错误为0

    # 迭代开始
    for i in range(iterations):
        error = 1 / (2 * m) * np.dot((np.dot(x, theta) - y).T,
                                     (np.dot(x, theta) - y))
        # 迭代停止
        if abs(error) <= threshold:
            break

        theta -= alpha / m * (np.dot(x.T, (np.dot(x, theta) - y)))

    print('多元变量：', '迭代次数：%d' % (i + 1), 'theta：', theta, 'error：%f' % error)


if __name__ == '__main__':
    bgd_single()
    bgd_multi()