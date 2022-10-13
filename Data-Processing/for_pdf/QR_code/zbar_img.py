from pyzbar.pyzbar import decode
from PIL import Image
from pikepdf import Pdf, PdfImage
import cv2

# pdf = Pdf.open('12.pdf')
# page = pdf.pages[0]
# keyimage = list(page.images.keys())
# rawimage = page.images[keyimage[0]]
# pdfimage = PdfImage(rawimage)

# img = pdfimage.as_pil_image()
# w, h = img.size
# img = img.crop((0, h/2, w, h))
from PIL import Image,ImageEnhance
img1 = Image.open('111.png')
img = cv2.imread('111.png')

decoded_data = decode(img)

for txt in decoded_data:
    barcodeData = txt.data.decode("utf-8")
    print(barcodeData)

# if decoded_data:
#     scan_CR = decoded_data[0].data.decode()
 