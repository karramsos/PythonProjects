#! /usr/bin/python

# About this snippet: Module for getting demographics from a website
# Author: Sukhvinder Singh | karramsos@gmail.com | @karramsos

from urllib import urlopen
from bs4 import BeautifulSoup
import re

def cleanHtmlRegex(i):
    i = str(i)
    regexPatClean = re.compile(r'<[^<]*?/?>')
    i = regexPatClean.sub('', i)
    i = re.sub('&\w+;','',i)
    return i

def demogSearch(regexSearch,i):
    demogResults = ''
    if re.search(regexSearch,str(i)):
        demogResults = re.search(regexSearch,str(i)).group().split('\n')
    
    return demogResults

# Searches multiple lines and then splits the data at the location of %
def multiLineRegex(regexSearch, i):
    multiLine = ''
    if re.search(regexSearch, str(i)):
        multiLine = re.search(regexSearch,str(i)).group().split('%')
    return multiLine

# Input the city and state to create the web address to search
cityName = raw_input('Enter the City Name?').replace(' ','-')
stateName = raw_input('Enter the State Name?').replace(' ','-')
searchCity = cityName + '-' + stateName
cityWebsite = 'http://www.city-data.com/city/' + searchCity + '.html'

# Copy all of the content to the Beautiful Soup Module
webpage = urlopen(cityWebsite).read()

# Pass the article to the Beautiful Soup Module
soup = BeautifulSoup(webpage)

# Tell Beautiful Soup to locate all of the p tags and store them in a list
paragList = soup.findAll('div')

# Set up all of the regular expressions
regexMale = re.compile('^Males.*$')
regexFemale = re.compile('^Females.*$')
regexAge = re.compile('(Median res.*)\n')
regexIncome = re.compile('Estimated.*:\s\$\d*,\d*')
regexEdu = re.compile('High school.*')
regexIndust = re.compile('Most common occupations.*', re.DOTALL)
regexRandom = re.compile('Estimated median house.*')

# Print all of the paragraphs to screen
for i in paragList:
    i = cleanHtmlRegex(i)

    allDemogs = []
    
    allDemogs += demogSearch(regexMale, i)
    allDemogs += demogSearch(regexFemale, i)
    allDemogs += demogSearch(regexAge, i)
    allDemogs += demogSearch(regexIncome, i)
    allDemogs += demogSearch(regexIndust,i)
    allDemogs += multiLineRegex(regexEdu,i)
    allDemogs += demogSearch(regexRandom,i)
    
    for m in allDemogs:
        print '1.' + m