import PyPDF2

file_path = r"C:\Users\meloc\Downloads\Cracking-Codes-with-Python.pdf"

with open(file_path, "rb") as file:
    pdf_reader = PyPDF2.PdfReader(file)
    text = "" 
    for page in pdf_reader.pages:
        text += page.extract_text()

print("PDF content")
print(text)

# Function taken from official PyPDF2 documentation

# https://pypdf2.readthedocs.io/en/3.x/user/extract-text.html

""" from PyPDF2 import PdfReader

reader = PdfReader(r"C:\Users\meloc\Downloads\Cracking-Codes-with-Python.pdf")
page = reader.pages[0]
print(page.extract_text()) """

