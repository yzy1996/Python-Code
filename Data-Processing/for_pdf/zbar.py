from pyzbar.pyzbar import decode

from pikepdf import Pdf, PdfImage

pdf = Pdf.open('12.pdf')
page = pdf.pages[0]
keyimage = list(page.images.keys())
rawimage = page.images[keyimage[0]]
pdfimage = PdfImage(rawimage)

decoded_data = decode(pdfimage.as_pil_image())

if decoded_data:
    scan_CR = decoded_data[0].data.decode()
