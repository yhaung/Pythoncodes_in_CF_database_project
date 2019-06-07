# modified from https://stackoverflow.com/questions/6011115/doc-to-pdf-using-python
# modified from img read https://www.geeksforgeeks.org/python-convert-image-to-pdf-using-img2pdf-module/
# modified by Kyaw Naing Win, OneMap GIS Program Manager
# convert all word files (doc and docx extension) in subdirectories to pdf under same sub-directories

import img2pdf 
from PIL import Image 
import sys
import os

# main directory
main_dir = r"D:\Programming\Python_Summary_for_OMM\Test"


# image file types
file_types = ["JPG","jpg"] # image file types

def list_files(pdir, file_types = []):                                                                                                  
    r = []                                           
    subdirs = [x[0] for x in os.walk(pdir)]
    for subdir in subdirs:              
        files = next(os.walk(subdir))[2]                  
        if (len(files) > 0):                                                        
            for file in files:
                if (len(file_types)):
                    for ftype in file_types:
                        if file.lower().endswith("."+ ftype):
                            r.append(subdir+ '\\' + file)
                else:
                    r.append(subdir+ '\\' + file)
                    
    return r

docs = list_files(main_dir, file_types)

# Convert to pdf

#word = comtypes.client.CreateObject('Word.Application')
#wdFormatPDF = 17 # pdf # for other types: https://docs.microsoft.com/en-us/dotnet/api/microsoft.office.interop.word.wdsaveformat?redirectedfrom=MSDN&view=word-pia

for doc_file in docs:
    pdf_path = doc_file[:-3]+"pdf"
    # opening image 
    image = Image.open(doc_file)
    
    # converting into chunks using img2pdf 
    pdf_bytes = img2pdf.convert(image.filename)
  
    # opening or creating pdf file 
    file = open(pdf_path, "wb") 
  
    # writing pdf files with chunks 
    file.write(pdf_bytes) 
  
    # closing image file 
    image.close() 
  
    # closing pdf file 
    file.close() 
    
    print(pdf_path)
  
    # output 
print("Successfully made pdf files")