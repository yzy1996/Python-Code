# 给txt每一行增加内容

with open('demo.txt') as f:
    lines = (line.strip() for line in f)
    for line in lines:
        print(line)