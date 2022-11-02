# Graham Payne
# AIST 2120, Lab 6 (Chapter 9)
# 10/12/2022

# Lab created by Hunter Thomas (Undergraduate Course Assistant). Modified
#     by Misty Lawrence (June 2021)

# ***************************************************************************
# The purpose of this lab is to practice reading and writing files.
#
#  Before writing any code, prepare the files:
#      1. Create a lab 9 folder on the desktop.
#      2. Save this file as lab5 Ch 9.py in your lab 9 folder.
# ***************************************************************************


# Welcome Banner

print('--------------------------------------'.center(60))
print('---           AIST 2120            ---'.center(60))
print('---   Lab Exercise 6, Chapter 9    ---'.center(60))
print('---           FileInator           ---'.center(60))
print('--------------------------------------'.center(60))
print()


# Import the operating system (os) module

import os


# Print the label for next step.  DO NOT CHANGE

print('The Current Working Directory is: ')


# Get the Current Working Directory (CWD) and then print it to the screen.
#      Is the CWD what you thought it would be?
#      Ensure it is the lab 9 folder placed on your desktop...

print("     " + os.getcwd())


# Create a string variable.  In it, place a title line indicating your schedule,
#     e.g., myHeader = "Justin's Schedule"

myHeader = "Graham's Schedule"



# Create an object in write mode for Sched_Hdr.txt.  Write to the file the
# variable holding the schedule header, and then close the file.  DO NOT CHANGE.

schedHdr_obj = open('Sched_Hdr.txt', 'w')
schedHdr_obj.write(myHeader)
schedHdr_obj.close()

print('\nStatus Update:')
print('     Created Sched_Hdr.txt with ' + myHeader +  'written to it.')


# Create a second file called Current_Sched.txt and open it in write mode.
# Write the title of this class (Scripting and Automation) to the file. 
# Close the file object.


schedCur_obj = open('Current_Sched.txt', 'w')
schedCur_obj.write('Scripting and Automation\n')
schedCur_obj.close()



# Write a status update for creating the second file.  DO NOT CHANGE.

print('\nStatus Update:')
print('     Created Current_Sched.txt and wrote Scripting and Automation to it.')


# Add the rest of your schedule to Current_Sched.txt.  Place each course on a
# separate line.  
#    Example: Calc 2
#             Data Structures
#             Klingon for Cool People
#             Operating Systems
#             Design and Maintenance of Warp Drive Engines
# Consider in what mode you should open the file object.  Close the file object.

schedCur_obj = open('Current_Sched.txt', 'a')
schedCur_obj.write("Data management\n")
schedCur_obj.write("Business Math\n")
schedCur_obj.write("Web Devlopment\n")
schedCur_obj.write("Networking & security\n")
schedCur_obj.close()



# Write a status update for creating the second file.  DO NOT CHANGE.

print('\nStatus Update:')
print('     Updated Current_Sched.txt with remaining course schedule.')


# Create Combo_File.txt in write mode and then close it to ensure the file
# is empty prior to writing to it.  STUDY, BUT DO NOT CHANGE.

comboFile_obj = open('Combo_File.txt', 'w')
comboFile_obj.close()

print('\nStatus Update:')
print('     Created empty file Combo_File.txt.')


# Re-open Combo_File.txt in append mode in preparation for file operations.

comboFile_obj = open('Combo_File.txt', 'a')


# Write a status update for opening file in append mode.  DO NOT CHANGE.

print('\nStatus Update:')
print('     Re-opened Combo_File.txt in append mode.')


# Place the contents of Sched_Hdr.txt and Current_Sched.txt into Combo_File.txt.
#      1.  Open file objects for the first two files (... in what mode?).
#      2.  Write them each to Combo_File.txt.

schedHdr_obj = open('Sched_Hdr.txt', 'r')
schedCur_obj = open('Current_Sched.txt', 'r')

for line in schedHdr_obj.readlines():
    comboFile_obj.write(line.strip()+"\n")

comboFile_obj.write('\n')

for line in schedCur_obj.readlines():
    comboFile_obj.write(line.strip()+"\n")

# Write a status update for writing to Combo_File.txt.  DO NOT CHANGE.

print('\nStatus Update:')
print('     Wrote both files to Combo_File.txt.  Write operations complete.')


# Close all file objects and then write a status update informing the user
# that all files have been closed.

schedHdr_obj.close()
schedCur_obj.close()
comboFile_obj.close()

print('\nStatus Updaate:\n     All files have been closed.')


#-----------------------------------------------------------------------
# Exit Message

print()
print('--------------------------------------'.center(60))
print('---   Lab Exercise 6, Chapter 9    ---'.center(60))
print('---            Complete            ---'.center(60))
print('--------------------------------------'.center(60))

#-----------------------------------------------------------------------
# End Lab Exercise 9
