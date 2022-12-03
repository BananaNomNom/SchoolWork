# Graham Payne
# AIST 2120, Lab 8, (Chapter 12)
# 11/29/2022
# Payne_lab_12.py

#  *** THANKS to UCA Justin Henry for developing this template.(6/2021) ***

# **********************************************************************
#
# For this lab you will follow along in chapter 12, pp. 286-290, of your
# book for the project titled "PROJECT: Downloading all XKCD Comics". 
# This is a web scraping script that will save a series of web comics
# into a file without you ever opening a browser window.
#
# **********************************************************************


print()
print('------------------------------------'.center(60))
print('---          AIST 2120           ---'.center(60))
print('---    Lab Exercise 8, Ch. 12    ---'.center(60))
print('---       Find the Funnies       ---'.center(60))
print('---     A.k.a., Web Scraping     ---'.center(60))
print('------------------------------------'.center(60))
print()


# Import statement(s)
#     Be sure to import any other modules needed.

import sys      # Import sys for clean exit

# importing more modules from the book
import requests, os, bs4

#-----------------------------------------------------------------------
# The layout in the book uses pseudocode to break the assignment into
# steps. In the step one code, you will see lines commented as TODO.
# These are the follow-on steps, so there is no need to include the TODO 
# lines in your code. As you progress, the number of TODOs will decrease 
# as you complete the steps associated with each consecutive TODO. Some
# steps will complete multiple TODOs.

# Because this is a follow on assignment, the most important thing will
# be comments demonstrating you understand what the code is doing and make 
# it simple for others to understand as well.  Use the descriptions the
# book gives to help you.

# Start by putting your step one code below.


# *** STEP 1:  Design the Program ***
# IMPORTANT IMPORTANT IMPORTANT!!!
# CHANGE while not url.endwith('#') TO while not url.endswith('00/')

# simple variable to store directory name
saveDir = "Payne_xkcd"

url = 'https://xkcd.com' # starting url
os.makedirs(saveDir, exist_ok=True) # store comics in ./xkcd

#this while loop will loop until the the comic url ending in 00/ is gotten to.
while not url.endswith('00/'):



# *** STEP 2:  Download the Web Page ***
# this is contained inside the while loop at the end of step 1

# Download the page.
    print('Downloading page %s...' % url)

    #requests the page and raises for status to check for errors
    res = requests.get(url)
    res.raise_for_status()

    #parses the page into a html
    soup = bs4.BeautifulSoup(res.text, 'html.parser')



# *** STEP 3:  Find and Download the Comic Image ***

    # Find the URL of the comic image.
    #this selects and <img> elements with the id of comic
    comicElem = soup.select('#comic img')
    
    #if else statement checking if the comic element is empty 
    if comicElem == []:
        print('Could not find comic image.')
    else:
        #downlaods the comic
        comicUrl = 'https:' + comicElem[0].get('src')
        # Download the image.
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()



# *** STEP 4:  Save the Image and Find the Previous Comic ***
        #this statement is still inside the else statemun from step 3
        # Save the image to ./xkcd. 
        #                   ^ above has been changed to save dir variable
        imageFile = open(os.path.join(saveDir, os.path.basename(comicUrl)),'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')



#-----------------------------------------------------------------------
# Exit banner and clean exit from program.

print()
print('--------------------------------'.center(60))
print('---      Lab Exercise 8      ---'.center(60))
print('---         Complete         ---'.center(60))
print("---  That, that's all folks! ---".center(60))
print('--------------------------------'.center(60))
print()

input('Press the ENTER key to exit')
sys.exit()

#-----------------------------------------------------------------------
# End of Lab Exercise 8 (Chapter 12)
