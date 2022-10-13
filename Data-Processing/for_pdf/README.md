# PDF 相关处理脚本

> 这里是一些基础用法，以及其他 [PDF OCR 识别](https://github.com/yzy1996/Python-Code/tree/master/Data-Processing/for_pdf/OCR)；[QR_code](https://github.com/yzy1996/Python-Code/tree/master/Data-Processing/for_pdf/QR_code)



**先说有哪些热门的库**

|                           名称                           |                            Stars                             |               最后更新时间（不带年份则表今年）               |                             特点                             |
| :------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|        [PyPDF2](https://github.com/py-pdf/PyPDF2)        | ![](https://img.shields.io/github/stars/py-pdf/PyPDF2?style=social) | ![](https://img.shields.io/github/last-commit/py-pdf/PyPDF2) |             基于pyPDF，纯python，支持超过10年了              |
| [pdfminer.six](https://github.com/pdfminer/pdfminer.six) | ![](https://img.shields.io/github/stars/pdfminer/pdfminer.six?style=social) | ![](https://img.shields.io/github/last-commit/pdfminer/pdfminer.six) |             基于PDFMiner，extracting information             |
|    [pdfplumber](https://github.com/jsvine/pdfplumber)    | ![](https://img.shields.io/github/stars/jsvine/pdfplumber?style=social) | ![](https://img.shields.io/github/last-commit/jsvine/pdfplumber) | Built on [pdfminer.six](https://github.com/pdfminer/pdfminer.six)，for detailed information about text character, rectangle, and line |
|      [PyMuPDF](https://github.com/pymupdf/PyMuPDF)       | ![](https://img.shields.io/github/stars/pymupdf/PyMuPDF?style=social) | ![](https://img.shields.io/github/last-commit/pymupdf/PyMuPDF) |       基于[MuPDF](https://mupdf.com/)，付费，C语言依赖       |
|      [pikepdf](https://github.com/pikepdf/pikepdf)       | ![](https://img.shields.io/github/stars/pikepdf/pikepdf?style=social) | ![](https://img.shields.io/github/last-commit/pikepdf/pikepdf) |     基于[QPDF](https://github.com/qpdf/qpdf)，C语言依赖      |
|        [pdfx](https://github.com/metachris/pdfx)         | ![](https://img.shields.io/github/stars/metachris/pdfx?style=social) | ![](https://img.shields.io/github/last-commit/metachris/pdfx) | Extract references (pdf, url, doi, arxiv) and metadata from a PDF |

**再说我比较推荐的库**，[PyPDF2](https://github.com/py-pdf/PyPDF2) and [pikepdf](https://github.com/pikepdf/pikepdf)

**安装方式**：

```shell
pip install PyPDF2
pip install pikepdf
```

**官网教程已经非常详细了**，在这里我只展示几个我常使用的脚本

- [pdf2img](#pdf2img)
- [extract_text](#extract_text)
- [extract_annotation](#extract_annotation)



## pdf2img

```python
from pikepdf import Pdf, PdfImage

with Pdf.open('1.pdf') as pdf:
    page = pdf.pages[0]
    keyimage = list(page.images.keys())
    rawimage = page.images[keyimage[0]]
    pdfimage = PdfImage(rawimage)

    # 保存为图片文件
    pdfimage.extract_to(fileprefix='test')

    # 保存为PIL.image
    img = pdfimage.as_pil_image()
    img.show()
```



## extract_text

```python
from PyPDF2 import PdfReader

reader = PdfReader("1.pdf")
page = reader.pages[0]
text = page.extract_text()

print(text)
```



## extract_annotation

```python
from PyPDF2 import PdfReader

reader = PdfReader("commented.pdf")

for page in reader.pages:
    if "/Annots" in page:
        for annot in page["/Annots"]:
            obj = annot.get_object()
            annotation = {"subtype": obj["/Subtype"], "location": obj["/Rect"]}
            print(annotation)
```











