# Pathlib 使用指南

> 背景介绍：不同的操作系统，会使用不同的斜杠来划分路径，

Different operation uses slash `/` and backslash(also called a hack, reverse slash) `\`



`\` 会表示很多转义的含义



`.` 表示当前路径，通常也可以省略

`..` 表示父目录



## New

```python
from pathlib import Path

data_folder = Path("source_data/text_files/")

file_to_open = data_folder / "raw_data.txt"
```



additional

```python
from pathlib import Path

filename = Path("source_data/text_files/raw_data.txt")

print(filename.name)
# prints "raw_data.txt"

print(filename.suffix)
# prints "txt"

print(filename.stem)
# prints "raw_data"

if not filename.exists():
    print("Oops, file doesn't exist!")
else:
    print("Yay, the file exists!")
```





```python
Path.cwd()  # 返回当前路径
Path.resolve()  # 将路径绝对化
```



## Old

```python
import os

data_folder = os.path.join("source_data", "text_files")

file_to_open = os.path.join(data_folder, "raw_data.txt")
```



使用 `pathlib` 进行路径的拆分



```python
from pathlib import Path

path = "/foo/bar/baz/file"
path_split = Path(path).parts
path_split
```

```python
('/', 'foo', 'bar', 'baz', 'file')
```



os.path.split 将文件路径和文件名分开

('/home/ubuntu/python', 'example.py')

.name .parent





与 os.path.split 的对照表

https://docs.python.org/zh-cn/3/library/pathlib.html#correspondence-to-tools-in-the-os-module









## 前缀 `stem` 和后缀 `suffix`

```shell
>>> PurePosixPath('my/library.tar').stem
'library'
```

```shell
>>> PurePosixPath('my/library.tar').suffix
'.tar'
```



## 修改前缀 `with_stem` & **修改后缀 `with_suffix`**

```shell
>>> p = PureWindowsPath('c:/Downloads/draft.txt')
>>> p.with_stem('final')
PureWindowsPath('c:/Downloads/final.txt')
```

```shell
>>> p = PureWindowsPath('README.md')
>>> p.with_suffix('.txt')
PureWindowsPath('README.txt')
```

