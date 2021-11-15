# Pythonic

让python代码更加优雅，也包含一些奇淫技巧

参考：[Google-Python语言规范](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_language_rules/)





## 1. 高效性

**f-string 用法**

```python
item = 1
print(f'the result is {item}') # f-string 用法
>>> the result is 1

# 保留精度
item = 1.23456
print(f'the result is {item:.3f}')
>>> the result is 1.235
```

**条件赋值**

```python
x = 3 if (y == 1) else 2
```

**使用with自动管理资源**

```python
# 不需要`file.close()`了
with open('filename') as f:
    for lines in f:
        print(lines)
```

**置换两个变量的值**

```python
a = 10
b = 5
a, b = b, a
```

**numpy数组大于1的值改为0**

```python
a = np.array([[1, 2, 3], [4, 5, 6]])
a[a > 2] = 0
print(a)
```





## 2. 可读性

**类型注解** ![python-version](https://img.shields.io/badge/python-≥3.5-blue)

传统的函数表示：

```python
def add(x, y):
	return x + y
```

加上类型注解后：

```python
def add(x:int, y:int) -> int:
	return x + y
```

> `: 类型` 指定参数类型，`-> 类型` 指定返回值类型
>
> 加上注解并没有校验功能，只是提示效果，增加可读性



## 3. 美观性

```python
print(' Beautiful '.center(40,'-'))
>>> -------------- Beautiful ---------------
```

```python
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
print(color.BOLD + 'Hello World !' + color.END) # 加粗print()输出的特定部分
```



`zfill()`



#### 主程序

开头都加上：`if __name__ == '__main__':`








### 向量矩阵

一律借助 `numpy`

```python
import numpy as np 

np.array([1,2,3]).shape # 一维数组
>>> (3,)
np.array([[1,2,3]]).shape # 二维数组
>>> (1,3)
np.array([[1],[2],[3]]).shape # 二维数组
>>> (3,1)
```

如果要使用@矩阵乘法，请用二维数组形式，避免使用一维数组形式



创建数组并赋值

一种是先创建个空的，可以初始化为0,1,随机数；分别对应的是 np.zeros(), np.ones(), np.empty()

然后再用切片的方式去重新赋值







### PySnooper调试

```python
import pysnooper

@pysnooper.snoop()
def func1():
    a = 0
    for i in range(2):
        a += 1

func1()
>>> 
Source path:... <ipython-input-22-530479303b4e>
15:51:55.512317 call         6 def func1():
15:51:55.512317 line         7     a = 0
New var:....... a = 0
15:51:55.512317 line         8     for i in range(2):
New var:....... i = 0
15:51:55.512317 line         9         a += 1
Modified var:.. a = 1
15:51:55.512317 line         8     for i in range(2):
Modified var:.. i = 1
15:51:55.512317 line         9         a += 1
Modified var:.. a = 2
15:51:55.512317 line         8     for i in range(2):
15:51:55.512317 return       8     for i in range(2):
Return value:.. None
```

---

## 奇淫技巧



### 合并列表

```python
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = sum(a,[])
print(b)
>>> [1, 2, 3, 4, 5, 6, 7, 8, 9]
```



### 生成器yield

在某些情况下用来替换函数中的 `return` ， [参考](https://liam.page/2017/06/30/understanding-yield-in-python/)

我们把数据看作是一个容器，在使用数据时，有时候是逐个获取其中的元素，这个过程叫[迭代]

可以在以下几种情况使用yield：

1、调用函数的结果时，需要用 for .. in ..形式，也就是把它看成一个生成器函数的时候

2、当函数中每次生成的值不一样时，之前我们会使用一个变量来存储，最后一起返回，这时候使用yield就可以不需要新变量，直接使用一个生成器



看一个输出斐波拉契数列前N项的例子

```python
# old method1 直接print输出
def fab(max): 
   n, a, b = 0, 0, 1 
   while n < max: 
       print(b)
       a, b = b, a + b 
       n = n + 1
    
fab(5)
>>> 1
 	1 
	2 
	3 
	5
```

```python
# old method2 先存到一个数组里
def fab(max): 
   n, a, b = 0, 0, 1 
   L = [] 
   while n < max: 
       L.append(b) 
       a, b = b, a + b 
       n = n + 1 
   return L
   
for n in fab(5):
	print(n)
>>> 1 
	1 
	2 
	3 
	5
```

```python
# new method
def fab(max): 
    n, a, b = 0, 0, 1 
    while n < max: 
        yield b 
        a, b = b, a + b 
        n = n + 1
        
for n in fab(5):
	print(n)
>>> 1 
	1 
	2 
	3 
	5
```



### 函数参数解包(unpacking)

列表前面加 星号 ：将列表解开成独立的元素作为形参

字典前面加 两个星号 ：是将字典解开成独立的元素作为形参

```python
def func1(a, b):
    return a + b
 
data = [4, 3]
print(func1(*data)) # equals to print(func1(4, 3))
>>> 7
```

```python
def func1(a, b):
    return a + b
 
data = {'a' : 4, 'b' : 3}
print(add(**data)) # equals to print(func1(4, 3))
>>> 7
```



### 同时输出元素和索引

```python
iterable = [5,4,3,2,1]

for i, item in enumerate(iterable):
    print(i, item)
>>> 0 5
	1 4
	2 3
	3 2
	4 1
    
for i, item in enumerate(iterable, 1): # 从1开始编号
    print(i, item)
>>> 1 5
	2 4
	3 3
	4 2
	5 1
```



### 按索引重新赋值

```python
import numpy as np 

a = np.array([9,8,7,6])
index = [0,1,2,3]
value = [0,1,2,3]
a[index] = value
print(a)
>>> [0 1 2 3]
```

```python
import numpy as np 

a = np.array([9,8,7,6])
index = [0,1,2,3,1] # 支持后来居上
value = [0,1,2,3,4]
a[index] = value
print(a)
>>> [0 4 2 3]
```



### for..else语法

else 放在循环里的含义是，如果循环全部遍历完成，没有执行break，则执行else

```python
for list in ['a', 'b', 'c']:
    if l == 'd':
        break
else:
    print('no d')
```





### 分享代码

#### 1 代码片段 snippet

[网站Carbon](https://carbon.now.sh/)

