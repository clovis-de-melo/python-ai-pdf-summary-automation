import PyPDF2

file_path = r"C:\Users\meloc\Downloads\Cracking-Codes-with-Python.pdf"

with open(file_path, "rb") as file:
    pdf_reader = PyPDF2.PdfReader(file)
    text = "" 
    for page in pdf_reader.pages:
        text += page.extract_text()

print("PDF content")
print(text)