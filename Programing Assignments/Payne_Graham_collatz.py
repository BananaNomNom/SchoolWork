# Graham Payne
# AIST 2120, Prog. Assignment 1
# 08/31/2022
# Payne_Graham_collatz.py

print()
print('--------------------------------'.center(60))
print('---        AIST 2120         ---'.center(60))
print('--- Programming Assignment 1 ---'.center(60))
print('---     Solution, Thisia     ---'.center(60))
print('---       Collatzinator      ---'.center(60))
print('--------------------------------'.center(60))
print()

# the collatz algorithm
def collatz(number):

    # trying to see if the number is even by testing of the remainder is 0
    if ((number % 2) == 0):
        number = number // 2
        print('The next number in the collatz sequence: ' + str(number))
        return number

    else:
        number = 3 * number + 1
        print('The next number in the collatz sequence: ' + str(number))
        return number

# this function recurses on itself in order to have the user input a compatible number
def userinput():
    test = int(input('Enter a positive number to Collatz: '))

    # validating that the user input is within parameters    
    if test > 0:
        print('The user chose ' + str(test) + ' to begin the Collatz.')
        print()
        return test

    else:
        print('[Hey! The Collatzinators only works with positive numbers.]')
        print ()
        return userinput()

# a while loop to not end until the collatz sequence returns a 1
tempNum = userinput()
while tempNum != 1:
    tempNum = collatz(tempNum)

print ()
print ()
print ()
print ('Collatz sequence is compete!')
print ()
print ()
print()
print('------------------------------------'.center(60))
print('---         Collatzinator        ---'.center(60))
print('---            Complete          ---'.center(60))
print('--- End Programming Assignment 1 ---'.center(60))
print('------------------------------------'.center(60))
print()