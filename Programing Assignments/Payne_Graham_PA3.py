#Graham Payne
#AIST 2120: PROGRAMMING ASSIGNMENT 3
#10/10/2022
#Payne_Graham_PA3.py

#imports
import os
import re

#Header/Footer Function
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
header = ['AIST 2120C','Programming Assignment 3','Fun With Files','Payne, Graham']
header_footer(header)

#MAIN PROGRAM

print("the current work directory is:\n\t\t" + str(os.getcwd()))

print("\nChecking for directories.")
for file in os.listdir(os.getcwd()):
    dir = os.path.join(os.getcwd(), file)
    if os.path.isdir(dir):
        print("\tConfirmed: " + str(file) + " Folder")

print()

#function to format the outputs of the text files
def textCombinator(pathTo):
    # windows testing
    if not os.path.exists(r".\Human_Resources\Payne_Graham_WVDogsConsolidated.txt"):
        outputFile = open(r".\Human_Resources\Payne_Graham_WVDogsConsolidated.txt", 'x')
    else:
       outputFile = open(r".\Human_Resources\Payne_Graham_WVDogsConsolidated.txt", 'a')

    #linux testing
    #if not os.path.exists(r"./Human_Resources/Payne_Graham_WVDogsConsolidated.txt"):
    #    outputFile = open (r"./Human_Resources/Payne_Graham_WVDogsConsolidated.txt", 'x')
    #else:
    #    outputFile = open (r"./Human_Resources/Payne_Graham_WVDogsConsolidated.txt", 'a')

    #opens file 
    file = open(pathTo, 'r')

    #get how many lines are in the text file
    lineLength = 0
    for line in file:
        line = line.strip()
        if len(line) > 0:
            lineLength += 1

    #adding back the two preffered spaces
    lineLength += 2

    #return file cursor to start of the file
    file.seek(0)

    #prints the first 2 lines
    for i in range(2):
        tempStr = file.readline().strip()
        print(tempStr)
        outputFile.write(tempStr + '\n')

    #formats and prints all lines between first 2 and last 2
    for j in range(lineLength-4):
        line = file.readline().strip()
        tab_po = re.compile(r'\*+')

        line1 = line.replace('\t','*')
        line2 = line.replace('\t','*')
        line3 = tab_po.sub(',,', line2)
        line4 = line3.split(',,')

        left, middle, right = line4
        tempStr = left.ljust(20,' ') + middle.ljust(30,' ') + right
        print(tempStr)
        outputFile.write(left.ljust(20,' ') + middle.ljust(30,' ') + right + '\n')

    #print last 2 lines
    for k in range(2):
        tempStr = file.readline().strip() + '\n'
        print(tempStr)
        outputFile.write(tempStr)
    
    #writing an extra line for posterity's sake
    outputFile.write('\n')

    file.close()
    outputFile.close()


# Windows testing
path = r'.\Regional_Files\WVDogsChasHR.txt'
path2 = r'.\Regional_Files\WVDogsAuburnHR.txt'

# Linux Testing
#   path = r'./Regional_Files/WVDogsChasHR.txt'
#   path2 = r'./Regional_Files/WVDogsAuburnHR.txt'

#===================================
#===         MAIN PROGRAM        ===
#===================================

# Windows
# Deletes the consolidated file if it already exists. 
if os.path.exists(r".\Human_Resources\Payne_Graham_WVDogsConsolidated.txt"):
    os.remove(r".\Human_Resources\Payne_Graham_WVDogsConsolidated.txt")

#Linux
# if not os.path.exists(r"./Human_Resources/Payne_Graham_WVDogsConsolidated.txt"):
#     os.remove(r"./Human_Resources/Payne_Graham_WVDogsConsolidated.txt")

#calling the function
textCombinator(path)
textCombinator(path2)

print("Writing consolidated data to file...")
print()
print('File added: Payne_Graham_WVDogsConsolidated.txt')
print()

#FOOTER!
footer = ['Fun With Files', 'Complete', 'End Programming Assignment 3']
header_footer(footer)