from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import requests

from pikepdf import Pdf, PdfImage

# with Pdf.open('test.pdf') as pdf:
#     page = pdf.pages[0]
#     keyimage = list(page.images.keys())
#     rawimage = page.images[keyimage[0]]
#     pdfimage = PdfImage(rawimage)

#     img = pdfimage.as_pil_image().convert("RGB")

# # load image from the IAM database
# url = 'https://fki.tic.heia-fr.ch/static/img/a01-122-02-00.jpg'
img = Image.open('test.png').convert("RGB")

processor = TrOCRProcessor.from_pretrained('microsoft/trocr-base-handwritten')
model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-base-handwritten')
pixel_values = processor(images=img, return_tensors="pt").pixel_values

generated_ids = model.generate(pixel_values)
generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

print(generated_text)