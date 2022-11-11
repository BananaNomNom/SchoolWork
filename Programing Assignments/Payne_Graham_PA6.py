#Graham Payne
#AIST 2120: Programming Assignment 6
#12/4/2022
#Payne_csv_json_ops.py

import os, shutil
import PyPDF2
import time
import json

#mode bools
testingMode = False
windowsMode = False

# [Do not Change]
def setup_destination_folder(lastN, file):
    '''This function creates a Destination Folder and
       places the assignments 00 - READ_ME.txt file in
       the directory. '''
    destination = lastN + '_Destination'
    try:
        os.mkdir(destination)
    except:
        pass
    shutil.copy(file, destination)
# [End of Do not Change]

#quick destination folder variable based on os mode
if windowsMode:
    destinationFolder = ".\\Payne_Destination\\"
else:
    destinationFolder = "./Payne_Destination/"

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


# Main
### ACTION REQUIRED: Replace lastN with your last name
my_last_name = 'Payne'

# Call the setup destination method. [Do not change]
setup_destination_folder(my_last_name, '00 - READ_ME.txt')

# Add Header
#Header
header = ['AIST 2120C','Graham Payne','Programming Assignment 6','PDF Encryptinator']
header_footer(header)

# Implement PA6, These snippets should help get you started 

print('\nProcessing folder: .\\Source\\\n')
#windows file
if windowsMode:
    sourceFiles = os.listdir('.\Source')
#linux file
else:
    sourceFiles = os.listdir('./Source')
print('Visible files found')
for item in sourceFiles:
    print(' -  ' + str(item))

print('\n\t\t----------------------------------------------------------------\n')

#PDF FINDING AND ENCRYPTION HERE

#removes items that do not have the .pdf filetype
for item in sourceFiles:

    if item.endswith('.pdf'):
        continue
    
    if testingMode:
        print('deleting file: ' + item)
    sourceFiles.remove(item)

# I dont know why but .docx files will not be removed unless specified in a different for loop
for item in sourceFiles:
    if item.endswith('.docx'):
        if testingMode:
            print('deleting file: ' + item)
        sourceFiles.remove(item)

#test print
if testingMode:
    print()
    print (sourceFiles)
    print()

print('Processed files location: ' + destinationFolder)

#dicitonary to latter become a json
timeDict = {}

print()
print('Processed files:')
#moving the pdf files
for item in sourceFiles:
    startTime = time.time()
    #windows
    if windowsMode:
        shutil.copy(".\\Source\\" + str(item),destinationFolder + str(item))
        readerPath = destinationFolder + str(item)

    #linux
    else:
        shutil.copy("./Source/" + str(item),destinationFolder + str(item))
        readerPath = destinationFolder + str(item)
    
    reader = PyPDF2.PdfFileReader(readerPath)
    writer = PyPDF2.PdfFileWriter()

    #adds all the pages from reader
    for page in reader.pages:
        writer.addPage(page)

    writer.encrypt('enigma')

    #writes to file
    with open(destinationFolder + 'encrypted_' + str(item), 'wb') as file:
        writer.write(file)

    endTime = time.time()
    #takes the difference of between start and end times and rounds to two decimal places
    howLong = round(endTime - startTime, 2)

    timeDict['encrypted_' + str(item)] = howLong

    print(' - encrypted_' + str(item))

    #removes the copied file
    os.remove(destinationFolder + str(item))

print('Created file: Payne_time_span.json')
#END BLOCK
if testingMode:
    print(timeDict)

#Making json
with open(destinationFolder + 'Payne_time_span.json', 'w') as jsonFile:
    #purposeful indentation
    json.dump(timeDict, jsonFile, indent=4)

print('\n\n')
print('*** Mission Complete ***')
print()

footer = ['Programming Assignment 6','PDF Encryptinator','Complete']
header_footer(footer)