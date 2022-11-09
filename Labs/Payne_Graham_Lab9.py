# Graham Payne
# AIST 2120
# 11/9/2022
#Payne_Graham_Lab9.py

#  *** THANKS to UCA Justin Henry for updating this lab. (6/2021) ***

# **********************************************************************
# Let's have some fun with PDF files and secret messages too.
# BIG HINT: MAKE SURE YOU ARE IN THE SAME DIRECTORY AS THE PDFs!!!
# **********************************************************************

# Welcome Banner

print()
print('------------------------------------'.center(60))
print('---          AIST 2120           ---'.center(60))
print('---    Lab Exercise 9, Ch. 15    ---'.center(60))
print('---          PDF POWER!          ---'.center(60))
print('------------------------------------'.center(60))
print()

# Import PyPDF2 and any other module(s) you may need.

import time
import PyPDF2
import sys
import os


#URL FOR TESTING!!!
#URL = '/home/banana/Desktop/Fall 2022/AIST-2120/Labs/lab9_Ch15 Lab/AIST 2120 Chapter 15 Files/'

#URL FOR SUBMITTING
URL = os.environ['USERPROFILE'] + '\\Desktop\\Example Files\\'

#--------------------------------------------------------------------------
# Salutation      DO NOT CHANGE

print ('Good morning, Mr. Phelps.')
       
       
# Located in the downloaded files is a file called 'encrypted.pdf'. Decrypt
# it; then print the contents of its first page to the screen without
# modifying it except for the modifications made by extractText() method.
# Note that this is possible, but you should see from this example that this
# is far from ideal.
# Note:  The decryption password is 'rosebud'.

reader = PyPDF2.PdfReader(URL + 'encrypted.pdf')

if reader.is_encrypted:
    reader.decrypt('rosebud')

print(reader.getPage(0).extractText())


# Combine 'meetingminutes.pdf', and 'meetingminutes2.pdf' into a single PDF
# called 'Combo.pdf'.

merger = PyPDF2.PdfMerger()

merger.append(URL + 'meetingminutes.pdf')

merger.append(URL + 'meetingminutes2.pdf')

merger.write(URL + 'Combo.pdf')
merger.close()

# Encrypt the watermark file. The password you should use is:
# 'West_Virginia'.  Name the encrypted version 'TS.pdf'.

reader = PyPDF2.PdfReader(URL + 'watermark.pdf')               
writer = PyPDF2.PdfWriter()

for page in reader.pages:
    writer.add_page(page)

writer.encrypt('West_Virginia')

output = open(URL + 'TS.pdf', 'wb')
writer.write(output)

output.close()


#-----------------------------------------------------------------------
# Exit banner and clean exit from program.

print()
print('--------------------------------'.center(60))
print('---      Lab Exercise 9      ---'.center(60))
print('---         Complete         ---'.center(60))
print('--------------------------------'.center(60))
print()
print ('This file will self-destruct in five seconds ... 5...')
time.sleep(1)
print ('  4 ...')
time.sleep(1)
print ('    3...')
print ()

input('Press the ENTER key to exit')
sys.exit()


#-----------------------------------------------------------------------
# End of Lab Exercise 9 (Chapter 15)
