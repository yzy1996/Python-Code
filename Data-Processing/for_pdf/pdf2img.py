import io
from PyPDF2 import PdfReader
from PIL import Image

# Open the PDF file and read all pages
pdf_file = open('1.pdf', 'rb')
pdf_reader = PdfReader(pdf_file)
pages = []
for i in range(pdf_reader.getNumPages()):
    page = pdf_reader.getPage(i)
    pages.append(page)

# Merge all pages into a single image
width = max(page.mediaBox.getWidth() for page in pages)
height = sum(page.mediaBox.getHeight() for page in pages)
image = Image.new('RGB', (width, height))
y = 0
for page in pages:
    x = (width - page.mediaBox.getWidth()) / 2
    img_bytes = bytes(page.getContents())
    try:
        img = Image.open(io.BytesIO(img_bytes)).convert('RGB')
    except TypeError:
        img = Image.open(io.BytesIO(img_bytes.decode())).convert('RGB')
    image.paste(img, (int(x), int(y)))
    y += page.mediaBox.getHeight()

# Convert the image to PNG format and save it
image.save('output.png', 'PNG')
