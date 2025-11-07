from docx2pdf import convert

# Input DOCX and output PDF
docx_file = "CV_Horace_converted.docx"
output_pdf = "CV_Horace_final.pdf"

# Convert DOCX to PDF
convert(docx_file, output_pdf)

print("Conversion completed:", output_pdf)
