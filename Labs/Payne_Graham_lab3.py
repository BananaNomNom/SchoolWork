# Graham Payne
# AIST 2120, Lab 3 (Chap. 5)
# 9/07/2021

# Originated by Steven Weldon. Modified by UCA Justin Henry (May 2021)

# **********************************************************************
# In this lab we will work with creating and modifying a dictionary.  
# **********************************************************************

# Welcome Banner

print()
print('--------------------------------'.center(60))
print('---        AIST 2120         ---'.center(60))
print('---      Lab Exercise 3      ---'.center(60))
print('---     Dictionary-inator    ---'.center(60))
print('--------------------------------'.center(60))
print()


# Import pretty print and sys

from cmd import PROMPT
import pprint
import sys

#-----------------------------------------------------------------------
# Enter Code Here
# Create a function, averageGrades, that computes the average grade
# of the dictionary # created below.  Use a docstrine to describe the
# purpose # of this function.
#    Hint: Come back and complete this after you build your dictionary below
#    Note: We want the following output. '\' is an escape character. 
#    The student\'s average across all classes is calculated_average 

def averageGrades(dictVar):
	# Takes a dictionary as input converst the values to a list then
	# averages the list
	# 
	# Input
	# -------------
	# dictVar: the input dictionary to be averages 
	# 
	# Output
	# -------------
	# average: the averaged result of the temporary list created from the dictionaries value

	tempList = dictVar.values()
	calculated_average = sum(tempList) / len(tempList)

	print("The student\'s average across all classes is " + str(calculated_average))


# ****** MAIN Program ******

# Create an empty dictionary named my_dictionary

my_dictionary = {}

# DO NOT CHANGE
# Printing the dictionary. 

print("Here's your empty dictionary:  ")
print(my_dictionary)
print()


# Enter Code Here
# Populate the dictionary with the following key-value pairs:
#       'Calc2', 97
#       'Elvish Language - Lord of the Rings', 78,
#       'Data Structures', 82
#       'Operating Systems', 88
#       'Key Raptor Natural History and Captive Management', 95

my_dictionary={'Calc2':97,
'Elvish Language - Lord of the Rings':78,
'Data Structures':82,
'Operating Systems':88,
'Key Raptor Natural History and Captive Management':95}



# DO NOT CHANGE
# Print the keys and values using the items() method.  Compare the output
# of your print statement with your neighbors.  Did they print in the same
# order? 

print("The dictionary Keys and Values added follow:")

for k, v in my_dictionary.items():
	print('     Key ' + str(k) + ' has Value ' + str(v))
	
print()

# Enter Code Here
# Check to see if 'Automation and Scripting' is in my_dictionary.  Print the
# result.

print("Is 'Automation and Scripting' in the dictionary?	" + str('Automation and Scripting' in my_dictionary))


 
#Enter Code Here
## Call the function you created earlier.
## Remember to pass it my_dictionary

averageGrades(my_dictionary)

 
# DO NOT CHANGE
# Notice the escape characters used to double space.
print('\n\n')           
print("The regular print of the dictionary follows.")

# Enter Code Here
# Print the dictionary using 'regular' print().

print(my_dictionary)

# # DO NOT CHANGE
# Place your code after the two print statements below.
print('\n\n')           
print("Here's a Pretty Print of the dictionary -- much better!")

# Enter Code Here
# Print the keys and values using Pretty Print.
#   Note the difference between this print and the earlier 'regular' print.

pprint.pprint(my_dictionary)

#-----------------------------------------------------------------------
# Exit Message

print()
print('--------------------------------'.center(60))
print('---    End Lab Exercise 3    ---'.center(60))
print('--------------------------------'.center(60))
print()
print()

#Enter Code Here
# Exit the program cleanly by a) prompting the user to press enter; b) then
# calling sys.exit() to pause until after the user presses enter.

input('Press ENTER to exit.')
sys.exit()


#-----------------------------------------------------------------------
# End of Lab Exercise 5
