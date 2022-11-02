#Graham Payne
#AIST 2120: Extra Credit
#12/4/2022
#Payne_Graham_bloganalyzer.py

# TODO:
# 1. Convert to regex from beautiful soup for the article finder
# 2. properly find the amazon ads
# 3. format output for assignment
#
#

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
header = ['AIST 2120C','Graham Solution','Extra Credit Assignment','Blog Analyzer']
header_footer(header)

#Code Start

#importing
from urllib.error import HTTPError
import requests
from bs4 import BeautifulSoup

class urlData:
    def __init__(self):
        self.amazonAd = 0
        self.googleAd = 0
        self.urlFound = []

    def toString(self):
        print("These are the url's found withing the article:")
        for article in self.urlFound:
            print("\t" + article)
        print()
        print("There are " + str(self.amazonAd) + " Amazon Ads in this article.")
        print()
        print("There are " + str(self.googleAd) + " Google Ads in this article.")

#function to find all article urls from a page.
#returns a list
def articleFinder(inputURL):

    try:    
        #requests from the url the html
        r = requests.get(inputURL)

        #parses it using beautifulsoup
    except HTTPError as e:
        print(e.response.text)

    #parses the requested text into html
    soup = BeautifulSoup(r.text, 'html.parser')

    #empty list for urls found from the root page
    articles = []

    #finds all <article> elements
    for article in soup.find_all('article'):
        #finds the first <a> element child of the <article> element
        #& gets the url from the <a> element from the article.
        articleURL = article.find('a', recursive=False).get('href')
        articles.append(articleURL)

    return articles

def articleScanner(inputURL):

    print("Scraping URL: " + inputURL)

    try:    
        #requests from the url the html
        r = requests.get(inputURL)

        #parses it using beautifulsoup
    except HTTPError as e:
        print(e.response.text)



    soup = BeautifulSoup(r.text, 'html.parser')

    parsedData = urlData()

    #finds all <article> elements
    for article in soup.find_all('article'):
        #finds the first <a> element child of the <article> element
        #& gets the url from the <a> element from the article.
        try:
            print("i tried")
            articleURL = article.find('a', recursive=True).get('href')
            parsedData.append(articleURL)
        except AttributeError:
            pass
        

    #counts all <div> tags that have the class 'adsbygoogle'
    for tempgoogAd in soup.find_all('ins',{'class':'adsbygoogle'}):
        parsedData.googleAd += 1

    #for tempamazAd in soup.find_all('a')
    #    if amazAd.get('href') == ""
    parsedData.toString()
    print()
    return parsedData

#function that will scan a url and provide a count of
#few variables to start it up
adTotalAmazon = 0
adTotalGoogle = 0
numArticleTotal = 0

rootURL = "https://grith-llc.com/blog/"

#scans the main page of articles
tierOneArticles = articleFinder(rootURL)
print("Here are the main pages blogs found: ")
for article in tierOneArticles:
    print('\t' + article)

print()

for article in tierOneArticles:
    tempVar = articleScanner(article)
    adTotalAmazon += tempVar.amazonAd
    adTotalGoogle += tempVar.googleAd
    numArticleTotal += len(tempVar.urlFound) + 1

print()
print("there are a total of " + str(numArticleTotal) + " articles.")
print()
print("there are a total of " + str(adTotalAmazon) + " Amazon Ads.")
print()
print("there are a total of " + str(adTotalGoogle) + " Google Ads.")

footer = ['Extra Credit Program','Mission Complete']
header_footer(footer)
