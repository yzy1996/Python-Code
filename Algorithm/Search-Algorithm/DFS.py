'''深度优先算法
算法逻辑：
从初始点开始，向子节点搜索，
'''


def iter_dfs(G, s):  # G是整个图， s是起点
    S, Q = set(), []  # S是存放具体的访问路径
    Q.append(s)  # Q是用来存放需要进行遍历的数据
    while Q:  # 只要不是空
        u = Q.pop()  # 删除并返回末尾元素
        if u in S:
            continue
        S.add(u)
        Q.extend(G[u])  # 在末尾追加
        yield u


if __name__ == "__main__":
    a, b, c, d, e, f, g, h, i = range(9)
    G = [
        {b, c, d, e, f},  # a
        {c, e},  # b
        {d},  # c
        {e},  # d
        {f},  # e
        {c, g, h},  # f
        {f, h},  # g
        {f, g}  # h
    ]
    print(list(iter_dfs(G, a)))  # [0, 5, 7, 6, 2, 3, 4, 1]
