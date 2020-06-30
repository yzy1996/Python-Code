import pikepdf

my_pdf = pikepdf.Pdf.open('test.pdf')
for page in my_pdf.pages:
   page.Rotate = 180
my_pdf.save('test-rotated.pdf')

