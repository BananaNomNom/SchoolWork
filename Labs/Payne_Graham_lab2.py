# Graham Payne
# 08/31/2022
# AIST 2120 Lab 2 (Chapters 3 & 4)

# Originiated by UCA Hunter Thomas.  Updated by UCA Justin Henry, 5/2021.

# **********************************************************************
# In this lab we will work with some functions that manipulate lists.  
# **********************************************************************

# Welcome Banner

print()
print('--------------------------------'.center(60))
print('---        AIST 2120         ---'.center(60))
print('---      Lab Exercise 2      ---'.center(60))
print('---    Functions and Lists   ---'.center(60))
print('--------------------------------'.center(60))
print()


#-----------------------------------------------------------------------
# Create a function to complete the following tasks:
#    1. Append the number 6 to the list.
#       Print the updated list with 6 appended to it.
#    2. Create a string with your name and capitalize every other letter,
#       e.g. JuStIn HeNrY.
#    3. Determine the number of capital letters in your name string.
#       Print the number of capital letters in your name string.
#    4. Determine the number of lowercase letters in your name string.
#       Print the number of lowercase letters in your name string.
# This function will be called in a later step.

def multiTasker(listParam: list):
    listParam.append(6)
    print('Our new lsit is: ' + str(our_list))

    myName = 'GrAhAm PaYnE'
    print('My input string is ' + myName)

    templist = list(myName)
    upCount = 0
    loCount = 0
    for i in range(len(templist)):
        if templist[i].islower():
            loCount += 1
        elif templist[i].isupper():
            upCount += 1

    print(str(upCount) + ' uppercase letters')
    print(str(loCount) + ' lowercase letters')
    
    return listParam



# ***** MAIN Program *****

# The initial list is created for you here.  DO NOT CHANGE.

our_list = []
for i in range (0,6):
    our_list.append(i)

print('Here is our list: ' + str(our_list))
print()


#  Call the function you created.  Remember to pass it the list.

our_list = multiTasker(our_list)

# Print only the last item of the list.




# Print the length of the list.

print("The List length is: " + str(len(our_list)))


# Remove the second item in the list and print the resulting list.

our_list.pop(1)
print("New List after deletion: " + str(our_list))


# Reverse the list, permanently, and print the result.

our_list.reverse()
print("The Flipped List: " + str(our_list))


#-----------------------------------------------------------------------
# Exit Message

print()
print('--------------------------------'.center(60))
print('---    End Lab Exercise 2    ---'.center(60))
print('--------------------------------'.center(60))
