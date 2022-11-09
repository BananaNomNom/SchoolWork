# Graham Payne
# AIST 2120, Lab 10  (Ch. 17)
# 11/9/2022
# Payne_Graham_Lab10.py


# In this lab you will create a Doomsday Device! Your device must be
# capable of 4 things.  (Updated 6/2021)

# 1. Your device must display when it was initiated.
# 2. Your device must display a countdown.
# 3. Your device must save a .txt file displaying the time the countdown
#    started and how long the countdown will last -- at the same time the
#    countdown begins(multi-threading).
# 4. Your device must display the time at which its countdown hits zero.

#### Your mission, whether or not you choose to accept it, was created by
#### UCA Justin Henry (April 2021).  Thank you, Justin!

#************************************************************************


# Welcome Banner
#--------------------------------------------------------------------------

print()
print('-----------------------------------------'.center(60))
print('---            AIST 2120              ---'.center(60))
print('---     Lab Exercise 10 (Ch. 17)      ---'.center(60))
print('---          Doomsday Device          ---'.center(60))
print('-----------------------------------------'.center(60))
print()

# Import statements
#--------------------------------------------------------------------------

import sys
import threading
import time
import datetime
import os


# Now produce the start time and begin your countdown while simultaneously
# breaking off a thread to save the necessary information.
#--------------------------------------------------------------------------

# Flavor text

print()
print('DOOOOOOOOOOOOOOOOOOOOOOOOOOOOM!  (Cue Mission Impossible Music Here)')
print()


# Create an integer to start countdown.  Also, obtain the time
# with the datetime module.  Display the current time for the user.

timestart = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
print("The time is " + timestart)
print()



# Create a function for the thread to run.
# To do so, define the function name, open the output file, and write
# the current time along with the number of seconds on the clock to
# the output file.  Close the file.

def timer():
    output = open('timer.txt', 'w')
    output.write(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
    output.write('\n13 seconds on the clock!')
    output.close()



# Create the calling code for the thread itself. (It executes in here)

threadObj = threading.Thread(target=timer)
threadObj.start()


# Write a while loop that counts down from 13 seconds on the clock (So unlucky).
# Ensure a second elapses between each countdown number (hint:  time.sleep).

i=13
while i >= 0:
    print(str(i) + ' seconds!')
    time.sleep(1)
    i -= 1





# Print more flavor text indicating the Doomsday device exploded.
#    YOU MUST CREATE YOUR OWN FLAVOR TEXT; NO COPYING.
#    Be creative and come up with your own flavor text.

print()
print('Welp time to get back to work.')


# End of lab and closing the program
#--------------------------------------------------------------------------

print('\n\n\n')
print('--------------------------------'.center(60))
print('-----     End of Lab 10    -----'.center(60))
print('- Wait, why are we still here? -'.center(60))
print('-             ...              -'.center(60))
print('-             ...              -'.center(60))
print('-             ...              -'.center(60))
print("-  Don't forget the sys.exit   -".center(60))
print('--------------------------------'.center(60))
print()

input('Press ENTER to exit')
sys.exit()

    
