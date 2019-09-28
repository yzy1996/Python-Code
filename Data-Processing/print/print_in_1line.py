# 同一行输出

import time
for i in range(20):
    time.sleep(0.4)
    print('\r',str(30-i).ljust(10),end='')


# import sys,time
# for i in range(20):
#     print('#',end='',flush=True)
#     time.sleep(0.4)

# 而 ‘\r‘ 则是回到当前的开头
# 默认是Flase，只有缓冲区满或者全部内容都获取到了，才会一次全部执行打印
# 改成True，就是强制刷新，立刻打印出来

# end='\n' 这个是默认的end参数，所以平时是打印一条之后会换行。
# 例子都将参数改为了空，所以不会换行了