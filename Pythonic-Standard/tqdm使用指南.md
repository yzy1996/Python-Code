# tqdm 使用指南

https://tqdm.github.io/



先不说原理了，直接上无脑的使用过方法：

```python
from tqdm import tqdm

epoch = 0

while epoch < 10:
    epoch += 1
    with tqdm(train_loader, desc=f'Epoch {epoch}/10') as pbar:
        for i, (images, _) in enumerate(pbar):

            pbar.set_postfix(loss=i)
```



再来说一下我们的目标：

- 在哪一个epoch
- 每一个epoch里的迭代iteration
- 

需要设置好一些说明，以及更新策略

如果 tqdm 内部是一个迭代器，

可迭代对象,与迭代器不同的是，我们可以遍历一个 range 对象而不「消耗」它：



主要是能够显示迭代训练的进度条，先来看基本功能

```python
from tqdm import tqdm

for char in tqdm(["a", "b", "c", "d"]):
    pass
```

因为 tqdm() 里的对象是一个 list，是一个可迭代对象，因此上述操作等价于

```python
from tqdm import tqdm

for char in ["a", "b", "c", "d"]:
    pass
```

所以这里先建立一种感觉，就是你第一遍还是写正常的迭代循环代码，然后改成tqdm进度条形式。



接着我们看一些更加复杂的例子

```python
# 有一个等价 range 的 trange

from tqdm import trange

# 等同于 for i in tqdm(range(10)):
for i in trange(10):
    pass
```

如果要给进度条加一点说明

```python
from tqdm import tqdm
from time import sleep

pbar = tqdm(["a", "b", "c", "d"])
for char in pbar:
    sleep(0.25)
    pbar.set_description("Processing %s" % char) # 出现在最前面
```

让上面代码更加优雅一点呢，似乎也并没有

```python
from tqdm import tqdm
from time import sleep

with tqdm(["a", "b", "c", "d"]) as pbar:
    for char in pbar:
        sleep(0.25)
        pbar.set_description("Processing %s" % char) # 出现在最前面
```

所以这里引入了一个 with ... as ... 结构，在python里实际是为了简化自动清理流程的，例如读取文件时候的open close

而这里如果 tqdm 内部是一个可迭代对象，则是会自动用完释放掉的，既然如此，那也就对应着没有自动释放掉的方法

```python
from tqdm import tqdm
from time import sleep

pbar = tqdm(total=100)
for i in range(10):
    sleep(0.1)
    pbar.update(10)
pbar.close()
```

上面代码的含义是，意思是每隔10步更新一次，每次更新10，所以进度条就是10+10+10... 这里替换为with结构的话就成了

```python
from tqdm import tqdm
from time import sleep

with tqdm(total=100) as pbar:
    for i in range(10):
        sleep(0.1)
        pbar.update(10)
```



再回去看例子2，到底有没有更加优雅的方式呢

```python
from tqdm import tqdm
from time import sleep

for char in (pbar := tqdm(["a", "b", "c", "d"])):
    sleep(0.25)
    pbar.set_description(f"Processing {char}") # 出现在最前面
```

利用了海象运算符，可以在 if 语句本身中声明并分配值

**这也是最推荐的一种使用样式！！！**



## 进阶细节

自定义初始值和总值

```python
from tqdm import trange
from time import sleep

epoch = 0
with trange(epoch, 10, initial=epoch, total=10) as pbar:
    for epoch in pbar:
        sleep(1)
```

`trange(start, end, initial, total)`



tqdm 后依旧是一个可迭代对象，因此可以继续放心搭配 enumerate 使用





 

 



