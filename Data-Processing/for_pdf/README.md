# PDF 相关

更多代码样例在 https://github.com/yzy1996/Python-Code/tree/master/Data-Processing/for_pdf



## 处理PDF

python下能够处理pdf的库有 PyPDF4(2018)，Mistune(2018)，pikepdf(2020)

因此最推荐的是使用[pikepdf](https://pikepdf.readthedocs.io/en/latest/index.html) （pike是梭子鱼的英文），安装也超简单，直接 `pip install pikepdf`



**官网教程已经非常详细了**，在这里我只展示几个我使用过的脚本



PDF转图像

```python
from pikepdf import Pdf, PdfImage

with Pdf.open('scan04.pdf') as pdf:
    page = pdf.pages[0]
    keyimage = list(page.images.keys())
    rawimage = page.images[keyimage[0]]
    pdfimage = PdfImage(rawimage)

    # 保存为图片文件
    pdfimage.extract_to(fileprefix='image_name')

    # 保存为PIL.image
    img = pdfimage.as_pil_image()
    img.show()
```



## PDF OCR 识别

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





## 识别二维码

> 写在这里，需要先将pdf转换成相应的图像格式

使用 [pyzbar](https://pypi.org/project/pyzbar/) 来帮助识别二维码，是经典的 **zbar** 在python3上的支持。

根据官方安装步骤，针对mac的错误`ImportError: Unable to find zbar shared library`需要额外的:

```shell
mkdir ~/lib
ln -s $(brew --prefix zbar)/lib/libzbar.dylib ~/lib/libzbar.dylib
```



基本用法（搬运自主页）

```python
# 使用 PIL.Image 类型
from pyzbar.pyzbar import decode
from PIL import Image

QR_info = decode(Image.open('name.png'))
QR_data = decoded_data[0].data.decode()
```

```python
# 使用 cv2 numpy.ndarray类型
from pyzbar.pyzbar import decode
import cv2

QR_info = decode(Image.open('name.png'))
QR_data = decoded_data[0].data.decode()
```



和pdf搭配起来的用法

```python
from pikepdf import Pdf, PdfImage
from pyzbar.pyzbar import decode

with Pdf.open('name.pdf') as pdf:
  page = pdf.pages[0]
  keyimage = list(page.images.keys())
  rawimage = page.images[keyimage[0]]
  pdfimage = PdfImage(rawimage)

	QR_info = decode(pdfimage.as_pil_image())
  if decoded_data:
      QR_data = decoded_data[0].data.decode()
```



