#Graham Payne
#AIST 2120: Extra Credit
#12/4/2022
#Payne_Graham_bloganalyzer.py

# TODO:
# 1. Convert to regex from beautiful soup for the article finder DONE
# 2. properly find the amazon ads DONE?
#   2a. properly finding google ads DONE?
#    2b. properly finding blog article urls DONE?
# 3. format output for assignment DONE
# 4. Provide a Access error output DONE
#

testingMode = True

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

#a list of words that do note denote an article
#used to filter urls
blacklist = ['amazon_products', '/product', '/products', '/shop', 
    '/category/', '/feed/', 'author', 'jacob-cox', 
    'about-us', '/blog', 'wp-', 'contact-us', '/cart', 
    'privacy', 'terms-of-use', '#']

#this is a class to store values allowing the extraction of 
#multiple datapoints from a function
class urlData:
    def __init__(self):
        self.amazonAd = 0
        self.googleAd = 0
        self.urlFound = []

    #testing method before I had the format down.
    #Abandoned
    def toString(self, adcount):
        print("These are the url's found withing the article:")
        for article in self.urlFound:
            print("\t" + article)
        if adcount == True:
            print()
            print("There are " + str(self.amazonAd) + " Amazon Ads in this article.")
            print()
            print("There are " + str(self.googleAd) + " Google Ads in this article.")

#function to find all article urls from a page.
#returns a list
def articleFinder(inputURL):
    
    #adds inputURL to blacklist
    blacklist.append(inputURL)
    
    #requests from the url the html
    try:    
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

    #removes all duplicates in the url list
    articles = [*set(articles)]

    #removes url from blacklist after done
    blacklist.remove(inputURL)

    return articles

#A function that scrapes the article for: 
#       Amazon ads, Google ads, and other articles
def articleScanner(inputURL):

    #adds inputURL to blacklist
    blacklist.append(inputURL)

    print("Analyzing URL: " + inputURL)
    #requests from the url the html
    try:    
        r = requests.get(inputURL)
        print("Access Issue: None") 
    except HTTPError as e:
        print(e.response.text)

    #parses it using beautifulsoup
    soup = BeautifulSoup(r.text, 'html.parser')

    parsedData = urlData()
    tempURL = ""

    #Copied and modified from the articleFinder() method
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
    

    #test amazon ad printout
    if testingMode:
        print('Amazon ad types + numbers:')

    #finds amazon ads
    #counts amazon ads using <img> elements that have the url amazon-adsystem.com in them.
    count = 0
    for tempamazAd in soup.find_all('img'):

        #I need this because apparently there are <img>
        #elements that do nto have a src attribute. which is strange
        try:
            tempamazAd = tempamazAd.get('src')
            if "ws-na.amazon-adsystem.com" in tempamazAd:
                if testingMode:
                    count += 1
                parsedData.amazonAd += 1
        except:
            continue
    
    #test print
    if testingMode:
        print('\t' + str(count) + 'x img')
    
    #counts amazon ads using <iframe> elements that have the url amazon-adsystem.com in them.
    count = 0
    for tempamazAd in soup.find_all('iframe'):
        try:
            tempamazAd = tempamazAd.get('src')
            if "ws-na.amazon-adsystem.com" in tempamazAd:
                if testingMode:
                    count += 1
                parsedData.amazonAd += 1
        except:
            continue 

    #test print
    if testingMode:
        print ('\t' + str(count) + 'x iframe')

    #due to suggestion I have added this to find another type of amazon ad found in blogs
    count = 0
    for tempamazAd in soup.find_all('a'):
        try:
            tempamazAd = tempamazAd.get('href')
            if "amazon.com/dp/" in tempamazAd:
                if testingMode:
                    count += 1
                parsedData.amazonAd += 1
        except:
            continue

    #test print
    if testingMode:
        print ('\t' + str(count) + 'x a')
        print()
        
    #finds google ads
    #counts all <ins> tags that have the class 'adsbygoogle'
    for tempgoogAd in soup.find_all('ins',{'class':'adsbygoogle'}):
        parsedData.googleAd += 1

    #testing print that reveals all urls before duplicates are removed
    if testingMode:
        print('Pre-consolidation URL list:')
        for item in parsedData.urlFound:
            print('\t'+item)
        print()

    #removes all duplicates in the url list
    parsedData.urlFound = [*set(parsedData.urlFound)]

    #test string retired
    if testingMode:
        parsedData.toString(adcount=False)

    #removes url from blacklist after done
    blacklist.remove(inputURL)

    #Printing Results
    print('Results:')
    print('\t... Blog URLs Detected:\t\t' + str(len(parsedData.urlFound)))
    print('\t... Amazon Ads Detected:\t' + str(parsedData.amazonAd))
    print('\t... Google Ads Detected:\t' + str(parsedData.googleAd))
    print()
    return parsedData

#function that will scan a url and provide a count of
#few variables to start it up
adTotalAmazon = 0
adTotalGoogle = 0
numArticleTotal = 0

#making a lists to house values to be used to count how many instances of pages have ads
perPageAmAd = []
perPageGoAd = []
perPageBlog = []

#root url that all other functions will be based on
rootURL = "https://grith-llc.com/blog/"
rootURL2 = rootURL + "page/2/"


#scans the main page for articles then stores them into a list
print("Evauluating Grith-LLC.com/blog")
print("Access Issue: None")

page1 = articleFinder(rootURL)
page2 = articleFinder(rootURL2)
tierOneArticles = page1 + page2

tierOneArticles = [*set(tierOneArticles)]

#prints out the the articles found from the list
print("Found " + str(len(tierOneArticles)) + " blogs on Grith-LLC's Blog Page")
for article in tierOneArticles:
    print('\t' + article)

print()

#scans each article for interested values
for article in tierOneArticles:
    tempVar = articleScanner(article)

    # takes the temperary object and extracts the useful information
    perPageAmAd.append(tempVar.amazonAd)
    adTotalAmazon += tempVar.amazonAd

    perPageGoAd.append(tempVar.googleAd)
    adTotalGoogle += tempVar.googleAd

    perPageBlog.append(len(tempVar.urlFound))
    numArticleTotal += len(tempVar.urlFound)


print()
print("Totals: ")
print("\tBlog Total: " + str(numArticleTotal))
print("\tAmazon Ad total: " + str(adTotalAmazon))
print("\tGoogle Ad total: " + str(adTotalGoogle))

print()
print("Averages Per Page: ")
print("\tBlogs: " + str(round(numArticleTotal/len(perPageBlog),2)))
print("\tAmazon Ads: " + str(round(adTotalAmazon/len(perPageAmAd),2)))
print("\tGoogle Ads: " + str(round(adTotalGoogle/len(perPageGoAd),2)))

footer = ['Extra Credit Program','Mission Complete']
header_footer(footer)
