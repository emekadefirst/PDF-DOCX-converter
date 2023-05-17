print('type in the name of the pdf you added to the folder in this format "file_name.pdf"')
pdf = input(">> ")
print('type in the name you want for the word document in this format "file_name.docx" ')
doc = input(">> ")

import os
from pdf2docx import Converter


def pdf_to_docx(input_path, output_path):
    cv = Converter(input_path)
    cv.convert(output_path)
    cv.close()


# Specify the input PDF file path
input_pdf_path = (pdf)

# Specify the output Word document path
output_docx_path = 'key.docx'

# Convert PDF to Word
pdf_to_docx(input_pdf_path, output_docx_path)

# Check if conversion was successful
if os.path.exists(output_docx_path):
    print("PDF successfully converted to Word.")
else:
    print("Conversion failed.")
