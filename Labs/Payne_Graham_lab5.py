# Graham PAyne
# AIST 2120, Lab 5 (Chapter 8)
# 10/2/2022

# Lab created by UCA Justin Henry with information from Misty Lawrence and
# Steve Weldon

# ***************************************************************************
# The purpose of this lab is to practice validating input using PyInputPlus.
# ***************************************************************************


# Welcome Banner

print('--------------------------------------'.center(60))
print('---           AIST 2120            ---'.center(60))
print('---   Lab Exercise 5, Chapter 8    ---'.center(60))
print('---         Input Insanity         ---'.center(60))
print('--------------------------------------'.center(60))
print()

#======================= DO NOT CHANGE =========================#
# Import pyinputplus and random below. For simplicity and to avoid
# confusion, please import pyinputplus as pyip. DO NOT CHANGE!

import pyinputplus as pyip
import random

# Three functions are defined below for you to use. DO NOT CHANGE!


# stringFlipper:  The string passed will have the words reversed, 
# capitalized, and spaces will be removed.

def stringFlipper (string_target):
    
    print()
    print('The string passed in is: ' + string_target)

    string_target = string_target.split()
    string_target.reverse()
    
    sep = ''
    string_target = sep.join(string_target)
    string_target = string_target.upper()

    print('The new string is -> ' + string_target)
    print()

    
# Counter:  The function will count the uppercase, lowercase, and numeric 
# characters in the string. Hopefully, this code looks familiar. 

def counter (check_string):

    print()
    print('The string passed in is: ' + check_string)
    print()
    
    countU = 0
    countL = 0
    countN = 0

    for i in check_string:
        
        if i.islower():
            countL += 1
            
        if i.isupper():
            countU += 1
            
        if i.isnumeric():
            countN += 1

    print('There are ' + str(countL) + ' lowercase letters.')
    print('There are ' + str(countU) + ' uppercase letters.')    
    print('There are ' + str(countN) + ' numeric symbols.')
    print()

    
# mathinatorPlus:  The sum, product, quotient, and difference of the 
# integers will be computed and displayed.

def mathinatorPlus (num1, num2):
    
    sum0 = num1 + num2
    prod = num1 * num2
    quot = num1 / num2
    diff = num1 - num2

    print()
    print('The integers passed in are', num1, 'and', num2)
    print()
    
    print('The sum is', sum0)
    print('The product is', prod)
    print('The quotient is', quot)
    print('The difference is', diff)
    print()


# =====> END OF GIVEN FUNCTIONS
#=======================================================================#

# ****** MAIN PROGRAM ******


# Use PyInpputPlus to request the user enter two integers. Both integers must
# be greater than or equal to -30 and less than or equal to 60. Allow the
# user no more than 2 attempts for the first integer and no more than 1
# attempt for the second integer. Default to the first integer as 8, and
# the second integer as -4 if no user entry is obtained.

inputOne = pyip.inputInt('Enter the first integer: ', limit=2,min=-30,max=60, default=8)

inputTwo = pyip.inputInt('Enter the second integer: ', limit=2,min=-30,max=60, default=-4)




# Call the mathinatorPlus function and pass it both integers.

mathinatorPlus(inputOne, inputTwo)




# Have the user input a number between 1 and 5; then have the user input
# his/her full name. The user has 2 attempts each for the number and for the
# string. The default number is 5 and the default string is 'Hank Hill'.
# Concatenate the user's number of random integers between 0 and 9
# to the user's name.


inputOne = pyip.inputInt('Enter a number between 1 and 5: ', limit=2,min=1,max=5, default=5)

inputTwo = pyip.inputStr('Enter your full name: ', limit=2, default='Hank Hill')


inputTwo += " "

for i in range(inputOne):
    inputTwo = inputTwo + str(random.randint(0, 9))



# Pass your string with the user's name and random numbers to the counter
# function.

counter(inputTwo)




# Prompt the user to enter a catchphrase. The user has 3 attemps. The
# phrase must only contain letters and spaces. No numeric characters are
# allowed. The default phrase is 'Dangit, Bobby!'.


inputOne = pyip.inputStr('Enter a catchphrase. Only letters and spaces: ',limit=3, blockRegexes=[r'^[^a-zA-Z\s]*$'], default='Dangit, Bobby!')



# Pass the catchphrase string to the stringFlipper function.

stringFlipper(inputOne)




#--------------------------------------------------------------------------
#Exit Message

print()
print('-------------------------------------------'.center(60))
print('---    END Lab Exercise 5, Chapter 8    ---'.center(60))
print('-------------------------------------------'.center(60))


    
