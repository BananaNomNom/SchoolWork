# Graham PAyne
# AIST 2120
# 10/19/2022
# Payne_Graham_lab7.py

# Lab created by UCA Justin Henry

# In this lab you will conduct several operations on files and directories.
# HINT: REMEMBER YOUR LAB ON FILES!
#--------------------------------------------------------------------------

print('--------------------------------'.center(60))
print('---        AIST 2120         ---'.center(60))
print('---      Lab Exercise 10     ---'.center(60))
print('---   Directory Operations   ---'.center(60))
print('---       and Logging        ---'.center(60))
print('--------------------------------'.center(60))
print()

# Import os, shutil, zipfile, and logging
#--------------------------------------------------------------------------

import os, shutil, zipfile, logging
import time

# Print the current working directory. If you are not in the test directory
# from D2L, you need to change directory into test. Use either an absolute
# or relative path, but include a comment with the opposite. For example,
# if my actual code has a relative path, my comment will be absolute.
#--------------------------------------------------------------------------
print("The current working directory is: \n\t" + os.getcwd())
print()
os.chdir(r'.\test')
print("The new current directory is: \n\t" + os.getcwd())
print()





# Enable logging for DEBUG messages.
#--------------------------------------------------------------------------

logging.basicConfig(filename='Debug.txt',level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


# Create a file in Test and write that the program has started as a DEBUG
# message. Name the file Debug.txt. Copy the Debug message to the file.
#--------------------------------------------------------------------------

logging.debug("Program has started")






# Now I will print a list of everything in Test. Zip the contents of
# Test into a zip file named Test2. Test2 must go in the same directory as
# Test. You will need to move everything after creating your zip file.
# HINT What do files, folders, and subfolders from the slides really
# represent? What are their data types? What data types can we write to a
# zip file?
#--------------------------------------------------------------------------

print("Files in the Test directory:")
for folderName, folders, files in os.walk(".\\"):
    print (files)
    


testZIP = zipfile.ZipFile("Test2.zip", 'a')
for file in files:
    testZIP.write(file, compress_type=zipfile.ZIP_DEFLATED)



# Close your zip file
#--------------------------------------------------------------------------
testZIP.close()
print()
print("Moving zip file to same directory as Test")
shutil.move('Test2.zip','..\\')

logging.shutdown()

# End Banner
#--------------------------------------------------------------------------

print()
print('That was kinda cool!')
print()
print('--------------------------------'.center(60))
print('---       End Exercise       ---'.center(60))
print('--------------------------------'.center(60))





