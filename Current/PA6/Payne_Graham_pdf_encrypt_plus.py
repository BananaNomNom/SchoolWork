#Graham Payne
#AIST 2120: Programming Assignment 6
#12/4/2022
#Payne_csv_json_ops.py

# TODO
# add threading to count how long the processing takes

import os, shutil
import re

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

print('\nProcessing folder: .\\source\\\n')
#windows file
#sourceFiles = os.listdir('.\Source')
#linux file
sourceFiles = os.listdir('./Source')
print('Visible files found')
for item in sourceFiles:
    print(' -  ' + str(item))

print('\n\t\t----------------------------------------------------------------')

#PDF FINDING AND ENCRYPTION HERE

#removes items that do not have the .pdf filetype
for item in sourceFiles:

    if item.endswith('.pdf'):
        continue

    #print('deleting file: ' + item)
    sourceFiles.remove(item)

# I dont know why but .docx files will not be removed unless specified in a different for loop
for item in sourceFiles:
    if item.endswith('.docx'):
        #print('deleting file: ' + item)
        sourceFiles.remove(item)

#test print
#print (sourceFiles)

#moving the pdf files
for item in sourceFiles:
    #windows
    #shutil.copy(".\\Source\\" + str(item),"\\Payne_Destination\\" + str(item))
    
    #linux
    shutil.copy("./Source/" + str(item),"/Payne_Destination/" + str(item))


#END BLOCK

print('\nProcessed files location: .\\Destination\\')



footer = ['Programming Assignment 6','PDF Encryptinator','Complete']
header_footer(footer)