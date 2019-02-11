# 示例代码：生成一个随机数并写入（每次重写）txt

import random
 
number = random.randint(1,10)

f = open('number.txt','w')
f.write(str(number))
f.close()