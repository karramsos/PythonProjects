#! usr/bin/python

# About this snippet: Example on conditionals and executables
# Author: Sukhvinder Singh | karramsos@gmail.com | @karramsos

yourAge = int(raw_input("How old are you: "))


if (yourAge > 0) and (yourAge < 120):
    if (yourAge == 35):
        print "Same as me"
    elif (yourAge > 35):
        print "Older than me" 
    else:
        print "Different from me"
else:
    print "Don't lie about your age" 
    
# Conditional Expressions

x, y = 1, 0

a = 'y is less than x' if (y<x) else 'x is less than y' 

print a