import numpy as np
# DNA_SIZE = 10            # DNA length
# POP_SIZE = 5           # population size
# pop = np.random.randint(2, size=(POP_SIZE, DNA_SIZE))
# print(pop)
# pop_copy = pop.copy()
# i_ = np.random.randint(0, POP_SIZE, size=1)  # 产生一个随机数 between 0-100

# cross_points = np.random.randint(0, 2, size=DNA_SIZE).astype(np.bool)   # astype转换数据类型，变成[True, False ..]
# print(cross_points)
# parent = pop[0]

# parent[cross_points] = pop[i_, cross_points]  # 实现了：cross_points中 True 的项 ，用 pop 中的替换 parent 的； 只有 True 的项才重新赋值

# print(parent)
# print(pop)


a = np.array([1,2,3,4,5])
print(a[np.array([1,2,1])])

# [1 0 0 1 1 1 1 1 1 1]
# [ True  True  True  True  True  True  True False False  True]
# [0 1 1 1 0 0 0 0 1 1]
# [0 1 1 1 0 0 0 1 1 1]