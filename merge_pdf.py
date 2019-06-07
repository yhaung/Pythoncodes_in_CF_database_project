# modified from https://stackoverflow.com/questions/3444645/merge-pdf-files
'''
from PyPDF2 import PdfFileMerger

pdfs = ['file1.pdf', 'file2.pdf', 'file3.pdf', 'file4.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(open(pdf, 'rb'))

with open('result.pdf', 'wb') as fout:
    merger.write(fout)
'''
import os
from PyPDF2 import PdfFileMerger
pdf_dir = os.getcwd()
pdf_merged_name = os.path.split(pdf_dir)[0]
pdf_merged_name = os.path.split(pdf_merged_name)[1] + ".pdf"
pdf_merged_name = pdf_dir + os.sep + pdf_merged_name
#pdf_merged_name = "result.pdf"

#pdf_dir = os.getcwd()

pdfs = []

for pdf in os.listdir(pdf_dir):
    if pdf[-3:]=='pdf' or pdf[-3:]== 'PDF':
        pdfs.append(pdf)

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(open(pdf, 'rb'))

with open(pdf_merged_name, 'wb') as fout:
    merger.write(fout)