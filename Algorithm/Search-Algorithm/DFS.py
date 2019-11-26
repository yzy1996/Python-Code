# 深度优先算法


def iter_dfs(G, s):  # G是整个图， s是起点
    S, Q = set(), []  # S是
    Q.append(s)
    while Q:
        u = Q.pop()
        if u in S: continue
        S.add(u)
        Q.extend(G[u])
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
