# 使用生成器表达式会非常高效，readline也不用了

with open('xxx.txt') as f:
    lines = (line.strip() for line in f)
    for line in lines:
        print(line)