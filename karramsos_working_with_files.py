#! /usr/bin/python
# About this snippet: Working with files example
# Author: Sukhvinder Singh | karramsos@gmail.com | @karramsos

import os

def retrieveFile():
    # Will catch any errors triggered if the file doesn't exist
    try:
        bestStudent = {}
        bestStudentStr = "The Best Students Ranked\n\n"
        
        # Will open the file studentgrades.txt and store it in the file f
        f = open('studentgrades.txt')
        
    # If the file isn't found a friendly error will print to screen
    except(IOError), e:
        
        print "File not found", e
        
    else:
        # Splits each line in the file into 2 strings
        # Creates a dictionary using those 2 strings as key value pairs
        for line in f:
            name, grade = line.split()
            bestStudent[grade] = name
            
        # Closes the file
        f.close()
        
        # Sorts the grades from the highest to lowest and stores them in a new string
        for i in sorted(bestStudent.keys(), reverse = True):
            print (bestStudent[i] + ' scored a ' + i)
            bestStudentStr += bestStudent[i] + ' scored a ' + i + '\n'
        
        print '\n'
        
        print bestStudentStr
        
        # Outputs the string to a new file 'w' stands for white to file
        outToFile = open('studentrank.txt', 'w')
        outToFile.write(bestStudentStr)
        
        # Closes the created file
        outToFile.close()
        
        print('Finished Update')
    
    return

def directoryPlay():
    
    # Outputs the files stored in directory / usr
    print os.listdir('/usr')
    
    # Checks if /usr/bin/python is a directory and then a file
    print os.path.isdir('/usr/bin/python')
    print os.path.isfile('/usr/bin/python')
    
    # Outputs all files in directory /usr
    dirList = os.listdir('/usr')
    
    # Cycles through files in /usr and outputs files if one of them is a directory
    for fil in dirList:
        if os.path.isdir('/usr/' + fil):
            print os.listdir('/usr/' + fil)
        else:
            continue
    
    # How to create a new directory and then how to delete it
    #os.mkdir('Users/karramsos/Documents/Testing')
    #os.rmdir('Users/karramsos/Documents/Testing') # Works if program has permission
    
    return

def main():
    retrieveFile()
    directoryPlay()

if __name__ == '__main__': main() 