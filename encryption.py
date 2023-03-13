#encrypts a pdf file
from PyPDF2 import PdfWriter, PdfReader
import os

name = input("enter the file name: ")
password = input("enter the password: ")

output = PdfWriter()
file = PdfReader(name)
n = len(file.pages)

for i in range(n):
    page = file.pages[i]
    output.add_page(page)

output.encrypt(password)

os.remove(name)
with open(name, "wb") as f:
    output.write(f)

    