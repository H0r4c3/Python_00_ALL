from pdf2docx import Converter

# Input PDF and output DOCX
pdf_file = "CV_Horace.pdf"
docx_file = "CV_Horace_converted.docx"

# Convert PDF to DOCX
cv = Converter(pdf_file)
cv.convert(docx_file, start=0, end=None)  # convert all pages
cv.close()

print("Conversion completed:", docx_file)
