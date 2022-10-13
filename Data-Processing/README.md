<h1 align="center">Data Processing</h1>
<div align="center">
整理处理txt、csv、docx、pdf 等的高效方法。这里记录一些最基本的用法，其他详细见对应子文件夹。

</div>

## 原则

`逗号`隔开的文件，尽量改为csv格式，因为处理csv格式有天然的优势

可以直接由txt文件格式转为csv格式



## 文件操作

对路径进行操作，推荐使用 [Pathlib](https://docs.python.org/3/library/pathlib.html)。

```python
# 获取当前文件夹所有pdf的文件名

from pathlib import Path

root_dir = Path('./')
pdf_list = sorted(root_dir.glob('*.pdf'))
```





