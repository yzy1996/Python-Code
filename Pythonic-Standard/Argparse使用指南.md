# Argparse使用指南

> argument parser 参数 解析器
>
> [官方介绍](https://docs.python.org/zh-cn/3/library/argparse.html)，先介绍的是不常用的ArgumentParser对象参数设定，后面才是常用的add_argument参数设定



## 基本使用只有三步：

- 创建解析

```python
import argparse
parser = argparse.ArgumentParser()
```

- 添加参数

```python
parser.add_argument("square", help="display a square of a given number", type=int)
```

- 解析参数

```python
args = parser.parse_args()
```

- 使用参数

```python
print(args.square ** 2)
```



## 详细讲如何添加参数



`add_argument()` 可以设置的选项非常多

```python
parser.add_argument([名称], action=[动作], nargs=[], const=[], default=[默认值], type=[参数类型], choices=[], required=[], help=[], metavar=[], dest=[])	
```

但最常用的是

```python
parser.add_argument('--square', type=int, default=1, help='display a square of a given number')
```

> 为了可读性，一般都是选择使用可选参数



### name

> 参数名是为了在使用时可以直接调用 `args.name`

有两种参数名的设置方式，差异体现在名称前有没有 `--` 或者 `-` (名称缩写的时候)

- 必写参数 (没有`-`)：按照设置的先后顺序对应读取，调用时不用写名称
- 可选参数 (有`-`)：可以无序读取，调用时要写名称



### type

> 默认是 `str`，指定为其他可以充当类型转换器



### default

> 当**可选参数**没有传入值时，使用默认值

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--square", type=int, default=1)
args = parser.parse_args()
print(args.square ** 2)
```

运行 `python use_argparse.py` 输出 `1`

运行 `python use_argparse.py --square 2` 输出 `4`



### help

> 用来描述这个参数的目的，执行 `-h` 或者 `--help` 时会显示



### action

> 指定了这个命令行参数应当如何被处理



支持的操作有（只介绍主要的，其余的看文档）：

- store

这是默认操作，我们能够使用参数，就是因为输入值被 `store` 在这个参数名里



- store_true / store_false

store_const 的特殊用法，存储 `True` 和 `False`



- append

储存一个列表，将每个参数值添加到列表中，一般是为了允许多次使用选项，只在可选参数时使用

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--foo")
args = parser.parse_args()
print(args.foo)
```

运行 `python use_argparse.py --foo 1 --foo 2` 输出 `2`

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--foo", action='append')
args = parser.parse_args()
print(args.foo)
```

运行 `python use_argparse.py --foo 1 --foo 2` 输出 `['1', '2']`



- count

> 计算一个关键字参数出现的次数

```
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-v', action='count', default=0)
args = parser.parse_args()
print(args.v)
```

运行 `python use_argparse.py -vvv` 输出 `3`

运行 `python use_argparse.py -v -v -v` 输出 `3`



### nargs

> 关联不同数目的命令行参数到单一动作，因为 `action` 是单一项目消耗单一命令行参数

- N：可以且必须传入 `N` 个参数，然后被聚集到一个列表中

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("foo", nargs=2)
args = parser.parse_args()
print(args.foo)
```

运行 `python use_argparse.py 1` 输出 `error`

运行 `python use_argparse.py 1 2` 输出 `['1', '2']`



- ？：首先从命令行中获取，若没有则从const中获取，仍然没有则从default中获取



- *、+：任意数量参数

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("foo", nargs='+')
args = parser.parse_args()
print(args.foo)
```

运行 `python use_argparse.py 1` 输出 `['1']`

运行 `python use_argparse.py 1 2` 输出 `['1', '2']`





---



通常 `Argparse` 都是在命令行，如果想要在脚本文件里直接调试怎么办呢？

**解析的时候把参数传进去**，像这样：

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('echo')
args = parser.parse_args(['hello world!'])
print(args.echo)
```

如果是可选参数

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--echo')
args = parser.parse_args(['--echo', 'hello world!'])
print(args.echo)
```

两者也可以结合起来