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

print(len(myfiles))
