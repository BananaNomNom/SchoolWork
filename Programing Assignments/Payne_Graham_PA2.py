# GRAHAM PAYNE
# AIST 2120
# 9/28/2022
# PAYNE_GRAHAM_PA2.py

# HEADER GOES HERE
temp = "="
temp = temp.center(54,'=')
print(temp)
temp = "AIST 2120"
temp = temp.center(54,'=')
print(temp)
temp = "PROGRAMMING ASSIGNMENT 2"
temp = temp.center(54,'=')
print(temp)
temp = "RegExinator"
temp = temp.center(54,'=')
print(temp)
temp = "SOLUTION, PAYNE"
temp = temp.center(54,'=')
print(temp)
temp = "="
temp = temp.center(54,'=')
print(temp)

print("\n == RegExinator Phone Number, Email, and Zip Code-inator == \n")

# IMPORTS
import pyperclip
import re

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

emailRegex = re.compile(r'[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}')

# REGEX FOR ZIP CODES

zipRegex = re.compile(r'\b\d{5}(?:[-\s]\d{4})?\b')


text = str(pyperclip.paste())

#stat variables for use later
phoneCount = 0
emailCount = 0
zipCount = 0

#finding matches from clipboard
clipboard = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    clipboard.append(phoneNum)
    phoneCount += 1

for group in emailRegex.findall(text):
    clipboard.append(group)
    emailCount += 1

for group in zipRegex.findall(text):
    clipboard.append(group)
    zipCount += 1

#if statement that will either print the results or "NO DATA :( if no matches are made."
if len(clipboard) > 0:
    #puts results into clipboard
    pyperclip.copy('\n'.join(clipboard))
    print("Data Copied to Clipboard\n")

    #Phone #'s section
    templist = clipboard[0:(phoneCount)]
    templist.sort()
    print("Phone Number Found: " + str(phoneCount))
    print('\n'.join(templist))
    print('\n')

    #Emails section
    templist = clipboard[(phoneCount):(phoneCount+emailCount)]
    templist.sort()
    print("Email Addresses Found: " + str(emailCount))
    print('\n'.join(templist))
    print('\n')

    #Zip Codes Section
    templist = clipboard[(phoneCount+emailCount):(phoneCount+emailCount+zipCount)]
    templist.sort()
    print("Zip Codes Found: " + str(zipCount))
    print('\n'.join(templist))
    print('\n')

else:
    print("NO DATA :(")

# FOOTER GOES HERE
temp = "="
temp = temp.center(54,'=')
print(temp)
temp = "RegExinator"
temp = temp.center(54,'=')
print(temp)
temp = "COMPLETE"
temp = temp.center(54,'=')
print(temp)
temp = "="
temp = temp.center(54,'=')
print(temp)