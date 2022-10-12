## PDF OCR 识别

使用python标准库做OCR识别。目前主流的库有这些，收集了Github上的Star数以及最新的更新日期。

|                             名称                             |                 更新时间（不带年份则表今年）                 |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
| [tesseract](https://github.com/tesseract-ocr/tesseract) ![](https://img.shields.io/github/stars/tesseract-ocr/tesseract?style=social) | ![](https://img.shields.io/github/last-commit/tesseract-ocr/tesseract) |
| [EasyOcr](https://github.com/JaidedAI/EasyOCR) ![](https://img.shields.io/github/stars/JaidedAI/EasyOCR?style=social) | ![](https://img.shields.io/github/last-commit/JaidedAI/EasyOCR) |
| [OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF) ![](https://img.shields.io/github/stars/ocrmypdf/OCRmyPDF?style=social) | ![](https://img.shields.io/github/last-commit/ocrmypdf/OCRmyPDF) |
| [pytesseract](https://github.com/madmaze/pytesseract) ![](https://img.shields.io/github/stars/madmaze/pytesseract?style=social) | ![](https://img.shields.io/github/last-commit/madmaze/pytesseract) |





使用 [ocrmypdf](https://ocrmypdf.readthedocs.io/en/latest/cookbook.html) ，根据[官方教程](https://ocrmypdf.readthedocs.io/en/latest/installation.html)安装。Linux系统（包含MacOS，WSL）会简单一点，Windows复杂一点。

本质上使用的是谷歌的tesseract工具，同时也有一个支持python的 https://github.com/madmaze/pytesseract

不过上述默认都不支持手写字，在学术上基于Transformer的技术也出现了，例如 https://github.com/microsoft/unilm/tree/master/trocr，https://github.com/Breta01/handwriting-ocr

使用方法：直接在命令行执行

```shell
ocrmypdf --pages 1 --optimize 0 --output-type none --sidecar output.txt input.pdf -
```

> --pages 1 是仅处理 pdf 的第一页，--optimize 0 禁用页面优化，--output-type none是不输出额外的一个pdf（需要配合最后的 -）
>
> 还可以加上 --quiet 不让打印过程

会在本地保存一个 output.txt 里面存有识别的文字。

> 默认的是英文，可以替换为其他语言



如果想要写入python，注意如果简单加进去会报一个错误 `python stdout is connected to a terminal. Please redirect stdout to a file.`下面的程序中已经修复了。

```python
import os
import subprocess
import shlex

file = 'test.pdf'
command = f"ocrmypdf --deskew --rotate-pages --rotate-pages-threshold 5 --output-type none --sidecar ocr_output.txt {file} -"
command_args = shlex.split(command)

with open('log', "w") as outfile:
    subprocess.run(command_args, stdout=outfile)
os.remove('log')
```







