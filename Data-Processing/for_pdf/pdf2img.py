from pikepdf import Pdf, PdfImage

with Pdf.open('scan.pdf') as pdf:
    page = pdf.pages[0]
    keyimage = list(page.images.keys())
    rawimage = page.images[keyimage[0]]
    pdfimage = PdfImage(rawimage)

    # 保存为图片文件
    pdfimage.extract_to(fileprefix='image_name')

    # 保存为PIL.image
    img = pdfimage.as_pil_image()
    img.show()