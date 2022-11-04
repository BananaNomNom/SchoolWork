#Graham Payne
#AIST 2120: Programming Assignment 5
#12/4/2022
#Payne_csv_json_ops.py

#importation!
import os
import re
import csv
import json
import datetime


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


#Header
header = ['AIST 2120C','Graham Solution','Programming Assignment 5','CSV and JSON Files']
header_footer(header)

#Code Start
print()
print("The current working directory is\n\t" + os.getcwd())
print()

print("Preparing to extract content and create csv file")
print('\t...Confirming Output directory exists')
if os.path.exists(r".\Output"):
    os.remove(r".\Output")
print("\t...Directory Created")
os.mkdir(r".\Output")

print()

def csvDoThings(pathTo):
    #opens file 
    file = open(pathTo, 'r')
    
    print("WVDogsNewHires.txt is ready for processing")

    tempList = []

    #get how many lines are in the text file
    lineLength = 0
    for line in file:
        lineLength += 1

    file.seek(0)

    for i in range(lineLength):
        #regex to replace all white spaces with a * char
        text = re.sub(r'\s+', '*', file.readline())
        #splits eache line based on the * char
        text = text.split('*')
        #appends first and second parts of the list
        tempList.append(text[0])
        tempList.append(text[1])

    file.close()

    #CSV writing
    with open('.\\Output\\CurrentEmpList.csv', 'w') as csvfile:
        print("CurrentEmpList.csv is ready to recieve data")
        print()

        employeeWriter = csv.writer(csvfile,lineterminator='\n')
        
        #simple while loop to make a small list in order to write it to the csv file
        i=0
        while (i < (len(tempList)-1)):
            text = [tempList[i], tempList[i+1]]
            i += 2
            employeeWriter.writerow(text)

    csvfile.close()

    print("Processing of CurrentEmpList.csv complete")
    print("\tFile Contains:")
    #CSV reading
    with open('.\\Output\\CurrentEmpList.csv', 'r') as csvfile:
        employeeReader = csv.reader(csvfile)
        
        for row in employeeReader:
            print('\t\t' + str(row))


    csvfile.close()
    
    print()
    print('Creating CurrentEmpList.json')
    jsonOutput = open('.\\Output\\CurrentEmpList.json', 'w')

    #gets current date data and puts it into a dictionary
    print('\t...Obtaining Data')
    timeDict = {
        "Year": str(datetime.date.today().year),
        "Month": str(datetime.date.today().month),
        "Day": str(datetime.date.today().day)
    }

    #converts the dictionary into a json format then writes to file
    print('\t...Writing content to file')
    json_object = json.dumps(timeDict, indent=4)
    jsonOutput.write(json_object)
    jsonOutput.close()

    #Verifying file
    print('Reading newly created JSON File')

    file = open('.\\Output\\CurrentEmpList.json', 'r')
    json_object = json.load(file)

    print('\tTodays date is ' + json_object['Month'] +'\/'+ json_object['Day'] +'\/'+ json_object['Year'])
    file.close()
    print('\tThe following content was written to CurrentEmpList.json')
    print('\t\t' + str(timeDict))
    print()
    print('processing of currentEmpList.json complete!')
    print()


csvDoThings(".\\WVDogsNewHires.txt")

footer = ['AIST 2120C','Programming Assignment 5','Complete']
header_footer(footer)