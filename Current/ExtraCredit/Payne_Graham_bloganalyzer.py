#Graham Payne
#AIST 2120: Extra Credit
#12/4/2022
#Payne_Graham_bloganalyzer.py

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
import requests
from bs4 import BeautifulSoup

class urlData:
    def __init__(self):
        self.amazonAd = 0
        self.googleAd = 0
        self.urlFound = []

    def toString(self):
        print("These are the url's found withing the article:")
        for article in urlFound:
            print("\t" + article)
        print()
        print("There are " + amazonAd + " Amazon Ads in this article.")
        print()
        print("There are " + googleAd + " Google Ads in this article.")

#function to find all article urls from a page.
#returns a list
def articleFinder(inputURL):
    #requests from the url the html
    r = requests.get(inputURL)

    #parses it using beautifulsoup
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

def articleScanner(inputURL)

    print("Scraping URL: " + inputURL)

    #requests from the url the html
    r = requests.get(inputURL)

    #parses it using beautifulsoup
    soup = BeautifulSoup(r.text, 'html.parser')

    parsedData = new urlData()

    #counts all <div> tags that have the class 'adsbygoogle'
    for tempgoogAd in soup.find_all('div',{'class':'adsbygoogle'})
        parsedData.googleAd += 1
        adTotalGoogle += 1

    #for tempamazAd in soup.find_all('a')
    #    if amazAd.get('href') == ""
    #         adTotalAmazon += 1

    parsedData.toString()

#function that will scan a url and provide a count of
#few variables to start it up
adTotalAmazon = 0
adTotalGoogle = 0
numArticleTotal = 0

rootURL = "https://grith-llc.com/blog/"

#scans the main page of articles
tierOneArticles = articleFinder(rootURL)
for article in tierOneArticles:
    articleScanner(article)
    numArticleTotal += 1

print()
print("there are a total of " + numArticleTotal + "articles.")
print()
print("there are a total of " + adTotalAmazon + "Amazon Ads.")
print()
print("there are a total of " + adTotalGoogle + "Google Ads.")

footer = ['Extra Credit Program','Mission Complete']
header_footer(footer)
