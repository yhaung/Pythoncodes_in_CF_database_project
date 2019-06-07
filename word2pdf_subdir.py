# modified from https://stackoverflow.com/questions/6011115/doc-to-pdf-using-python
# modified by Kyaw Naing Win, OneMap GIS Program Manager
# convert all word files (doc and docx extension) in subdirectories to pdf under same sub-directories
import sys
import os
import comtypes.client

# main directory

main_dir = r"C:\WingPy_scripts\comtypes"

# word file types
file_types = ["doc","docx"] # word file types

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
word = comtypes.client.CreateObject('Word.Application')
wdFormatPDF = 17 # pdf # for other types: https://docs.microsoft.com/en-us/dotnet/api/microsoft.office.interop.word.wdsaveformat?redirectedfrom=MSDN&view=word-pia

for doc_file in docs:

    if doc_file.lower().endswith(".docx"):
        pdf = doc_file[:-4]+"pdf" 
    else:
        pdf = doc_file[:-3]+"pdf"
        
    doc = word.Documents.Open(doc_file)
    doc.SaveAs(pdf, FileFormat=wdFormatPDF, EmbedTrueTypeFonts=True)
    doc.Close()
    print (pdf+" created")

word.Quit()
print ("word to pdf coversion completed") 