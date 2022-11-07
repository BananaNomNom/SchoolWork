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

#a list of words that do note denote an article
#used to filter urls
blacklist = ['/product-category',
    '/product',        
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

    #requests from the url the html
    try:    
        r = requests.get(inputURL)
        print("Access Issue: None")

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
    return articles

#A function that scrapes the article for: 
#       Amazon ads, Google ads, and other articles
def articleScanner(inputURL):

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


        #the next two blocks filter for the domain urls inside a <a> elements href
        #adding a count to the number of amazon ads and ending this iteration
        #if "amazon-adsystem.com" in articleURL:
        #    parsedData.amazonAd += 1
        #    continue
        
        
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
                    
    #finds amazon ads
    #counts amazon ads using <img> elements that have the url amazon-adsystem.com in them.
    for tempamazAd in soup.find_all('img'):
        #print('I found an image')

        #I need this because apparently there are <img>
        #elements that do nto have a src attribute. which is strange
        try:
            tempamazAd = tempamazAd.get('src')
            #print(tempamazAd)

            if "ws-na.amazon-adsystem" in tempamazAd:
                #print ('+1')
                parsedData.amazonAd += 1
        except:
            continue

        
        
    #finds google ads
    #counts all <ins> tags that have the class 'adsbygoogle'
    for tempgoogAd in soup.find_all('ins',{'class':'adsbygoogle'}):
        parsedData.googleAd += 1

    #test string retired
    parsedData.toString(adcount=False)

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

#scans the main page for articles then stores them into a list
print("Evauluating Grith-LLC.com/blog")
tierOneArticles = articleFinder(rootURL)

#prints out the the articles found from the list
print("Found " + str(len(tierOneArticles)) + "blogs on Grith0LLC's Blog Page")
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
