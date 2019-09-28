"""
Visualize Genetic Algorithm to find a maximum point in a function.
Visit my tutorial website for more: https://morvanzhou.github.io/tutorials/
"""
import numpy as np
import matplotlib.pyplot as plt

DNA_SIZE = 10            # DNA length
POP_SIZE = 100           # population size
CROSS_RATE = 0.8         # mating probability (DNA crossover)
MUTATION_RATE = 0.003    # mutation probability
N_GENERATIONS = 200
X_BOUND = [0, 5]         # x upper and lower bounds


def F(x): return np.sin(10*x)*x + np.cos(2*x) * \
    x     # to find the maximum of this function


# find non-zero fitness for selection
def get_fitness(pred): return pred + 1e-3 - np.min(pred)


# convert binary DNA to decimal and normalize it to a range(0, 5)
# x**y 返回 x 的 y 次幂
def translateDNA(pop): return pop.dot(2 ** np.arange(DNA_SIZE)
                                      [::-1]) / float(2**DNA_SIZE-1) * X_BOUND[1]


# 适者生存 nature selection wrt pop's fitness
def select(pop, fitness):
    # 从np.arange(POP_SIZE)中产生一个大小为 size 的随机数组（可以有重复），p 是选择对应元素的概率（概率越大抽中次数越多）
    idx = np.random.choice(np.arange(POP_SIZE), size=POP_SIZE, replace=True,
                           p=fitness/fitness.sum())
    return pop[idx]

# DNA交叉配对，两个 DNA, True 的点我们取 DNA1 中的元素, False 的点取 DNA2 中的. 生成的 DNA3 就有来自父母的基因了
def crossover(parent, pop):
    if np.random.rand() < CROSS_RATE:  # 产生一个随机数
        i_ = np.random.randint(0, POP_SIZE, size=1)  # 产生一个随机数 between 0-100
        cross_points = np.random.randint(0, 2, size=DNA_SIZE).astype(np.bool)   # astype转换数据类型，变成[True, False ..]
        parent[cross_points] = pop[i_, cross_points]  # 只有 True 的项才重新赋值；同时pop也被改变了，与parent对应的相同了
    return parent

# DNA变异
def mutate(child):
    for point in range(DNA_SIZE):
        if np.random.rand() < MUTATION_RATE:
            child[point] = 1 if child[point] == 0 else 0
    return child


# initialize the pop DNA 生成一个 0 1 的矩阵， 100*10
pop = np.random.randint(2, size=(POP_SIZE, DNA_SIZE))

plt.ion()       # 连续画图
x = np.linspace(*X_BOUND, 200)
plt.plot(x, F(x))

for _ in range(N_GENERATIONS):
    # compute function value by extracting DNA
    F_values = F(translateDNA(pop))

    # something about plotting
    if 'sca' in globals():
        sca.remove()
    sca = plt.scatter(translateDNA(pop), F_values, s=200, lw=0, c='red', alpha=0.5)
    plt.pause(0.05)

    # GA part (evolution)
    fitness = get_fitness(F_values)
    print("Most fitted DNA: ", pop[np.argmax(fitness), :])
    pop = select(pop, fitness)
    pop_copy = pop.copy()  # 一定要复制
    for parent in pop:
        print((pop_copy==pop).all())
        child = crossover(parent, pop_copy)  # 
        child = mutate(child)
        parent[:] = child       # parent is replaced by its child
        

plt.ioff()
plt.show()
