# 识别二维码



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







