from pyzbar.pyzbar import decode
from PIL import Image
from pikepdf import Pdf, PdfImage


pdf = Pdf.open('2.pdf')
page = pdf.pages[0]
keyimage = list(page.images.keys())
rawimage = page.images[keyimage[0]]
pdfimage = PdfImage(rawimage)
img = pdfimage.as_pil_image()

# img = pdfimage.as_pil_image()
# w, h = img.size
# img = img.crop((0, h/2, w, h))
# img.show()

# img = cv2.imread('ttest.jpg')
decoded_data = decode(img)

print(decoded_data)

# if decoded_data:
#     scan_CR = decoded_data[0].data.decode()
