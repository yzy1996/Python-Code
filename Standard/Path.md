# Something about Path

Different operation uses slash `/` and backslash(also called a hack, reverse slash) `\`



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





