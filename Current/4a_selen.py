# Selenium Program Example
# By Jacob Cox
# 4a_selen.py
'''
# Review
- https://pypi.org/project/selenium/
- https://selenium-python.readthedocs.io/navigating.html
- https://selenium-python.readthedocs.io/locating-elements.html
- https://selenium-python.readthedocs.io/
This code requires the geckodriver.exe driver for Firefox
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.get('https://inventwithpython.com')

seconds = 2   # Use this for sleep times
close = True  # Change this to False to leave browser open

time.sleep(seconds+2)

# Selenium can locate elements by texts
try:
    # Use inner html
    text_link = 'Python Programming Exercises, Gently Explained' 
    elem = browser.find_element(By.LINK_TEXT, text_link)
    print('First: \n', elem)
    elem.click()
except:
    print('Failed: ', text_link)

time.sleep(1)

# Selenium can locate elements by XPATH
try:
    xpath_amz = '/html/body/div[2]/div[2]/div[13]/div/p/a[1]'
    elem = browser.find_element(By.XPATH, xpath_amz)
    print('\nSecond: \n', elem)
    elem.click()
except:
    print('\nFailed: ', xpath_amz)
time.sleep(seconds+1)

try:
    print('\nThird: Backing Up\n')
    browser.back()
    time.sleep(seconds)
    browser.refresh()
except:
    print('\nCouldn\'t go back\n')
time.sleep(seconds)

# Locate element by CSS Selector and tag name and print content. 
try: 
    css_select = 'div.row:nth-child(12) > div:nth-child(2)'
    elem = browser.find_element(By.CSS_SELECTOR, css_select)
    # Locate paragraph tags within elem and print text
    print('Fourth: Trying Select: \n', elem.find_element(By.TAG_NAME,'p'))
    content = elem.text
    content = content.split('\n')
    print('first paragraph'.center(40,'-'), '\n')
    print(content[0])
    print('\n', '--'.center(40,'-'))
    
    print("\nHere are some other options we could have selected:")
    print(dir(elem))
    print()
    print("\nYou can also always use help to find current features:")
    print(help(elem))
    print('That is all!'.center(40,'-'))
except Exception as e:
    print(e)


if close == True:
    browser.close()
    browser.quit()
