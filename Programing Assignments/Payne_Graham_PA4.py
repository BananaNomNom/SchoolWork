#Graham Payne
#AIST 2120: PROGRAMMING ASSIGNMENT 4
#10/17/2022
#Payne_Graham_PA4.py

#imports
import sys
import re
import os
import shutil
import zipfile
import pyinputplus as pyip
import pyperclip

# useful functions
'''
This assignment will require you to use regular expressions, file
management, and more. To help you with your assignement, I've included
multiple functions I used in this assignments solution. You may use
some or all of them in yours.


os.getcwd()
os.listdir()
pyip.inputNum()
sys.exit()
print(('-'*40).center(50,' '))
for line in input_fh.readlines():
    Do Stuff
build_a_string = 'Here is some text followed by new lines.\n\n'+ \
             'a \ after a plus (+) lets us extend to a ne line \n\n' +\
             'you can also insert varialbes like this \n\n' + phones + \
             '\n or: \n' + emails + \
             '\n or something else \n' + dates
os.path.isdir(r'')
os.mkdir(r'')
os.unlink(r'')
shutil.copy('')
os.chdir('') - you want to change directories before writing your zip file
newZip = zipfile.ZipFile('solution_zip.zip', 'a')
newZip.write(item)
'''

# So where should you begin? I would try copying the tasks from programming
# assignment 4 and use them as my comments and build one section at a
# time adding additional comments. . 

#Header/Footer Function
#taken from Prog assignment 3 and edited to fit the assignment
def header_footer(input):
    tempInt = 0
    for item in input:
       tempInt = 0

       if len(item) > tempInt:
           tempInt = len(item)
    
    baseWidth = 60
    miniWidth = 40

    print("".center(baseWidth,'-'))

    for item in input:
        print((str(item).center(miniWidth, ' ')).center(baseWidth, '-'))
    
    print("".center(baseWidth,'-'))


#Header!
header = ['AIST 2120C','Graham Solution','Programming Assignment 4','Regexinator Plus']
header_footer(header)

print()
print("*** Welcome to Regexinator Plus ***")
print()
print("I'm going to ask you to let me know if your file is in this folder. \n\tI'll take care of the rest...")
print()

#taken from Prog assignment 3 and edited to fit the assignment
print("You are working in the following directory:\n\t\t" + str(os.getcwd()))

#taken from Prog assignment 3 and edited to fit the assignment
print("\nThese files are in your current working directory.")
for file in os.listdir(os.getcwd()):
    dir = os.path.join(os.getcwd(), file)
    if os.path.isdir(dir):
        print("\tFound: " + str(file) + " Folder")
    #newly added
    else:
        print("\tFound: " + str(file))

print()

if not pyip.inputInt("Did you see your file? ",min=0,max=1):
    sys.exit()

print()

title = ['Regexinator Plus Engaged']
header_footer(title)

print()
print("here are the matches...")
print()

#open contact file
file = open("ContactInfo.txt", 'r')

#STOLEN CODE FROM PROGRAMMING ASSIGNMENT 2 EDITED
# REGEX FOR PHONE #'s

phoneRegex = re.compile(r'''(
    \b(\d{3}|\(\d{3}\))?# area code
    (\s|-|\.)?# separator
    (\d{3})# first 3 digits
    (\s|-|\.)# separator
    (\d{4})# last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?# extension
    )''', re.VERBOSE)

# REGEX FOR EMAILS

emailRegex = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')

# REGEX FOR DATES
#newly added
dateRegex = re.compile(r'\b\d{1,2}\/\d{1,2}\/\d{2,4}\b')


text = ''

for line in file.readlines():
    text += line

#stat variables for use later
phoneCount = 0
emailCount = 0
dateCount = 0

#finding matches from matches EDITED
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
    phoneCount += 1

for group in emailRegex.findall(text):
    matches.append(group)
    emailCount += 1

for group in dateRegex.findall(text):
    matches.append(group)
    dateCount += 1

#newly added output file instead of clipboard
outputFile = open('Payne_Graham_output.txt', 'w')
outputFile.write("here are the matches...\n")

#if statement that will either print the results or "NO DATA :( if no matches are made."
if len(matches) > 0:
    #Phone #'s section
    templist = matches[0:(phoneCount)]
    templist.sort()

    outputFile.write("These phone numbers were found: \n")
    for item in templist:
        outputFile.write(item + "\n")
    outputFile.write("\n")

    print("These phone numbers were found: ")
    print('\n'.join(templist))
    print('\n')

    #Emails section
    templist = matches[(phoneCount):(phoneCount+emailCount)]
    templist.sort()

    outputFile.write("These emails were found: \n")
    for item in templist:
        outputFile.write(item + "\n")
    outputFile.write("\n")

    print("These emails were found: ")
    print('\n'.join(templist))
    print('\n')

    #Zip Codes Section
    templist = matches[(phoneCount+emailCount):(phoneCount+emailCount+dateCount)]
    templist.sort()

    outputFile.write("These dates were found:\n")
    for item in templist:
        outputFile.write(item + "\n")
    outputFile.write("\n")

    print("These dates were found:")
    print('\n'.join(templist))
    print('\n')

else:
    print("NO DATA :(")

#END OF STOLEN CODE

print()
print("pattern matches sent to file Payne_Graham_output.txt")
print()

file.close()
outputFile.close()


# makes a directory
os.mkdir(".\\Payne_PA4")

# moves/copies files to the directory
try:
    shutil.move(".\\Payne_Graham_output.txt",".\\Payne_PA4\\Payne_Graham_output.txt")
except:
    print("Failed to move file")
    sys.exit()

try:
    shutil.copy(".\\ContactInfo.txt",".\\Payne_PA4\\ContactInfo.txt")
except:
    print("Failed to copy file")
    sys.exit()

try:
    shutil.copy(".\\Payne_Graham_PA4.py",".\\Payne_PA4\\Payne_Graham_PA4.py")
except:
    print("Failed to copy file")
    sys.exit()

os.chdir(".\\Payne_PA4")

# zipping folder
    #Deprecated
    #littleList = []
    #for item in os.listdir(os.getcwd()+"\\Payne_PA4"):
    #    littleList.append(item)
    #
    #os.chdir(".\\Payne_PA4")
    #
    #finalZIP = zipfile.ZipFile("Payne_PA4.zip", 'w')
    #for item in littleList:
    #    finalZIP.write(item)

# os walks and returns list of files
littleList = ''
for folderName, folders, files in os.walk(".\\"):
    littleList = files

# debug command
#print(littleList)

#add files from the previous os walk list to zipfile
zipFile = zipfile.ZipFile("Payne_PA4.zip", 'a')
for file in files:
    zipFile.write(file, compress_type=zipfile.ZIP_DEFLATED)

zipFile.close()
#move file to parent folder
shutil.move('Payne_PA4.zip','..\\')

# up to parrent folder
os.chdir("..\\")

#remove the temporary folder
shutil.rmtree(".\\Payne_PA4")

print()
print("Archive solution_zip.zip created.")

#footer!
footer = ['AIST 2120C','Programming Assignment 4','Mission Complete']
header_footer(footer)