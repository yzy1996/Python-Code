import matplotlib.pyplot as plt
import numpy as np


def pareto_front(x, y):
    b = []
    i = 0
    while i < len(x):
        j = 0
        while j < len(a):
            if i != j:
                vj1 = a[j][0]
                vj2 = a[j][1]
                vi1 = a[i][0]
                vi2 = a[i][1]

                if (vj1 >= vi1 and vj2 <= vi2) and (vj1 > vi1 or vj2 < vi2):
                    i += 1
                    break
                else:
                    j += 1
                if j == len(a):
                    print(a[i])
                    i += 1
                    break
            else:
                j += 1
                if i == len(a)-1 and j == len(a):
                    print(a[i])
                    i += 1


# 帕累托最优点需要满足左下区域没有其他点
# 遍历Traversal
# 数据点表示为 (x[i],y[i])
for i = range(len(x)):
    for j = range(len(x)):
        if x[j]>=x[i] & y[j]>=y[i]:
            pareto_optimality=[x[i],y[i]]



def plot_pareto():
    plt.plot(p1, p2, 'ro')


if __name__ == '__main__':

    x = np.array([2, 5, 1, 3, 2, 7])
    y = np.array([9, 8, 12, 11, 16, 10])
    plt.plot(x, y, 'ro')
    plt.show()


# 加上可视化
