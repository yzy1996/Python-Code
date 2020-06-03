from docx import Document

file = Document("demo.docx")

for para in file.paragraphs:
    print(para.text)