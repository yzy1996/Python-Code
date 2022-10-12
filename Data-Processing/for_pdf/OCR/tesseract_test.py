
import pytesseract
from pikepdf import Pdf, PdfImage

with Pdf.open('wrong2.pdf') as pdf:
    page = pdf.pages[-1]
    keyimage = list(page.images.keys())
    rawimage = page.images[keyimage[0]]
    pdfimage = PdfImage(rawimage)

    img = pdfimage.as_pil_image()
    w, h = img.size
    # img = img.crop((0, 0, w/2, h/3))

print(pytesseract.image_to_string(img, lang='chi_sim'))
# print(pytesseract.image_to_osd(img))