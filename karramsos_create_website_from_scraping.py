#! /usr/bin/python

# About this snippet: Create a HTML page after scraping a webpage
# Author: Sukhvinder Singh | karramsos@gmail.com | @karramsos

from urllib import urlopen
from bs4 import BeautifulSoup
import re

print 'Content-type: text/html'
print  '<html><head>'
print 'Huffington Post Feed'
print '</head><body>'

def cleanHtml(i):
    i = str(i) # Convert the Beautiful Soup Tag to a string
    bs = BeautifulSoup(i) # Pass the string to Beautiful Soup to strip out html
    
    # Find all of the text between paragraph tags and strip out the html
    i = bs.find('p').getText()
    
    # Strip ampersand codes and WATCH:
    i = re.sub('&\w+;','',i)
    i = re.sub('WATCH:','',i)
    return i

def cleanHtmlRegex(i):
    i = str(i)
    regexPatClean = re.compile(r'<[^<]*?/?>')
    i = regexPatClean.sub('', i)
    # Strip ampersand codes and WATCH:
    i = re.sub('&\w+;','',i)
    return re.sub('WATCH:','',i)
    
# Copy all of the content from the provided web page
webpage = urlopen('http://feeds.huffingtonpost.com/huffingtonpost/LatestNews').read()

# Grab everything that lies between the title tags using a REGEX
titleString = '<title>(.*)</title>'
patFinderTitle = re.compile(titleString)

# Grab the link to the original article using a REGEX
origArticleLink = '<link rel.*href="(.*)" />'
patFinderLink = re.compile(origArticleLink)

# Store all of the titles and links found in 2 lists
findPatTitle = re.findall(patFinderTitle, webpage)
findPatLink = re.findall(patFinderLink, webpage)

# Create an iterator that will cycle through the first 16 articles and skip a few
listIterator = []
listIterator[:] = range(2,16)

# Print out the results to screen
for i in listIterator:
    print '<h3>' + findPatTitle[i]+'</h3><br />' # The title
    print "<a href ='" + findPatLink[i] + "'>Original Article</a><br />" # The link to the original article
    print '\n'
    articlePage = urlopen(findPatLink[i]).read() # Grab all of the content from original article
    
divBegin = articlePage.find('<div>') # Locate the div provided
article = articlePage[divBegin:(divBegin+1000)] # Copy the first 1000 characters after the div
    
# Pass the article to the Beautiful Soup Module
soup = BeautifulSoup(article)
    
# Tell Beautiful Soup to locate all of the p tags and store them in a list
paragList = soup.findAll('p')
    
# Print all of the paragraphs to screen
for i in paragList:
    # i = cleanHtml(i)
    i = cleanHtmlRegex(i)
    print i + '<br />'

print '<br /></body></html>'