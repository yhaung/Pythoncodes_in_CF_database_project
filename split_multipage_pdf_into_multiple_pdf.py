
#https://stackoverflow.com/questions/490195/split-a-multi-page-pdf-file-into-multiple-pdf-files-with-python


import PyPDF2
from PyPDF2 import PdfFileWriter, PdfFileReader
filename = r"D:\mgw_CFpermitsFD_OMM\cf_permits\ntmk_023_KyunBoke\scan\ntmk_023_KyubBoke.pdf"
inputpdf = PdfFileReader(open(filename, "rb"))

outfile =
for i in range(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    with open("document-page%s.pdf" % i, "wb") as outputStream:
        output.write(outputStream)
        print("successfully converted")