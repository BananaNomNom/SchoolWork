#Graham Payne
#AIST 2120: Programming Assignment 5
#12/4/2022
#Payne_csv_json_ops.py

#importation!
import os
import csv


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

os.mkdir(r".\Output")





footer = ['AIST 2120C','Programming Assignment 5','Complete']
header_footer(footer)