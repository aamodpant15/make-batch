
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 12:28:29 2020

@author: Aamod Pant
"""

import sys
import os

#save command line argument as name of the file to create file
batname=sys.argv[1] #batch file name to create
# batname='testfile'


content='@ py C:\\Aamod\\Python_Programs\\py_files\\ %*'
print("Add pause? y/n")
answer=input()
if(answer.lower()=="y"):
    content=content+'\n@ pause'

# creating content for batch file
breakpoint=content.index('%')-1
content= content[:breakpoint]+batname+'.py'+content[breakpoint:]
path= content[5: (content.rindex('\\py_files'))+1]+batname+'.bat'

print(path)

#creating batch file, and checking if file exists
if not os.path.exists(path):
      newf= open(path, 'w+')
      newf.write(content)
      newf.close()
      print("File created")
else:
    print('File already exists')
    

#Batch file created