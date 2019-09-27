

#https://stackoverflow.com/questions/46184239/python-extract-a-page-from-a-pdf-as-a-jpeg
import os, subprocess,time

pdf_dir = r"D:\mgw_CFpermitsFD_OMM\Python_Scripts\test"
os.chdir(pdf_dir)

pdftoppm_path = r"C:\Program Files\poppler-0.68.0\bin\pdftoppm.exe"


for pdf_file in os.listdir(pdf_dir):

    if pdf_file.endswith(".pdf"):
        outfile = pdf_file[0:-4]

        #subprocess.Popen('"%s" -jpeg %s ye' % (pdftoppm_path, pdf_file))
        subprocess.Popen('"{}" -jpeg {} {}'.format(pdftoppm_path, pdf_file,outfile))
        print("successfully converted")
time.sleep(3) 


for jpg in os.listdir(pdf_dir):
    if jpg.endswith(".jpg"):
        new_jpg = jpg[0:-6]+".jpg"
        print(new_jpg)
        os.rename(pdf_dir+"\\"+jpg,pdf_dir+"\\"+new_jpg)
            
        print(pdf_dir+"\\"+jpg,pdf_dir+"\\"+new_jpg)
  