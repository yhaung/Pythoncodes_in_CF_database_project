#This code is modified from Ko Kyaw Naing Win pdfghost_00.py you can downlaod here (https://github.com/yhaung/My_python_used_in_project/blob/master/pdfghost_00.py)

import os
import sys
import subprocess

maindir =r"D:\test"

# listing all files in subdirectoires

def list_files(dir):                                                                                                  
    r = []                                                                                                            
    subdirs = [x[0] for x in os.walk(dir)]                                                                            
    for subdir in subdirs:                                                                                            
        files = os.listdir(subdir)
        if (len(files) > 0):                                                                                          
            for file in files:
                if file.endswith((".pdf",".PDF")):
                        r.append(subdir + "\\" +file)
                        print (subdir + "\\" +file)
    return r
myfiles =list_files(maindir)


# ghostscript exe path
gs_cmd = r"C:\Program Files\gs\gs9.27\bin\gswin64c.exe"

# folders

 #--loop through subdirectories and all files end in  .pdf and .PDF

for x in myfiles:
    
    cmd_args = []
    sub_cmds = "-sDEVICE=pdfwrite -dCompatibilityLevel=2 -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH -sOutputFile="
            
    #ghostscript -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/printer -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf input.pdf
        
    #cmd_args += (gs_cmd, sub_cmds, output_pdf, input_pdf)
    cmds = (gs_cmd + " " +sub_cmds+x[:-4]+"_mobile.pdf"+" "+x)
    subprocess.run(cmds)

    print ("\n"+x+" successfully reduced file size..")
