with open('example.txt') as f:
    lines = (line.strip() for line in f)  # 得到一个迭代器
    for line in lines:
        print(line)