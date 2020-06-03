# 将列表写入txt
import numpy as np
a = [1, 2, 3]

np.savetxt('11.txt', a, fmt='%i', delimiter=',')
    