
import pytesseract
from pikepdf import Pdf, PdfImage

with Pdf.open('scan.pdf') as pdf:
    page = pdf.pages[0]
    keyimage = list(page.images.keys())
    rawimage = page.images[keyimage[0]]
    pdfimage = PdfImage(rawimage)

    img = pdfimage.as_pil_image()

print(pytesseract.image_to_string(img))
# print(pytesseract.image_to_osd(img))