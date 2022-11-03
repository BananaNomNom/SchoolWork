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
from bs4 import BeautifulSoup
import re
import requests


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

#a list of words that do note denote an article
#used to filter urls
blacklist = ['product-category',        
    'products',
    'shop',
    'category',
    'authors',
    'author',
    'comment',
    'jacob-cox',
    'about-us',
    'blog',
    'wp-login',
    'contact-us',
    'cart',
    'privacy-policy-2',
    'terms-of-use']

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
    tempURL = ""

    #finds all <a> elements
    for article in soup.find_all('a', recursive=True):
        #gets the href value from the <a> element
        articleURL = article.get('href')

        #first a statement that makes sure the url has the specified domain.
        if bool(re.match(r'https://grith-llc\.com/.*', articleURL)):

            #makes sure the url doesn't have any word that is also in the blacklist
            if not any(word in articleURL for word in blacklist):

                #filters out urls that are only the based domain
                if not bool(re.match(r'^https:\/\/grith-llc\.com\/$', articleURL)):

                    #filters out duplicates that may exist from same parent
                    if not articleURL == tempURL:

                        #finaly appends it to a list of articles
                        articles.append(articleURL)
                        tempURL = articleURL

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
    tempURL = ""


    #finds all <a> elements
    for article in soup.find_all('a', recursive=True):
        #gets the href value from the <a> element
        articleURL = article.get('href')

        #first a statement that makes sure the url has the specified domain.
        if bool(re.match(r'https://grith-llc\.com/.*', articleURL)):

            #makes sure the url doesn't have any word that is also in the blacklist
            if not any(word in articleURL for word in blacklist):

                #filters out urls that are only the based domain
                if not bool(re.match(r'^https:\/\/grith-llc\.com\/$', articleURL)):

                    #filters out duplicates that may exist from same parent
                    if not articleURL == tempURL:
                        
                        #finaly appends it to a list in the parsedData object
                        parsedData.urlFound.append(articleURL)
                        tempURL = articleURL
                    

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

#scans the main page for articles
tierOneArticles = articleFinder(rootURL)
print("Here are the main pages blogs found: ")
for article in tierOneArticles:
    print('\t' + article)

print()

#scans each article for interested values
for article in tierOneArticles:
    tempVar = articleScanner(article)

    # takes the temperary object and extracts the useful information
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
