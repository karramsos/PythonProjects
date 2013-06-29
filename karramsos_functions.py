#! /usr/bin/python

# About this snippet: Examples on variuos functions and usage
# Author: Sukhvinder Singh | karramsos@gmail.com | @karramsos

# Define a docstring a special function attribute
globalVariable = 10

def addNumbers(NumOne=1, NumTwo=2):
    'Adds the numbers passed to the function'
    return NumOne + NumTwo

def addUndefNums(NumOne=1, NumTwo=1,*args):
    'Adds the numbers passed to the function'
    finalValue = NumOne + NumTwo
    if args:
        for i in args:
            finalValue += i
        return finalValue
    else:
        return finalValue

def scopeFunction():
    mainNumber = 10
    print id(mainNumber)
    print "mainNumber equals", mainNumber, "in function scopeFunction"
    return

def changeGlobal():
    globals()['globalVariable'] = 20
    return

def createDict(**kvargs):
    for i in kvargs:
        print i, kvargs[i]
        print type(kvargs[i])
        print type(kvargs)
        print kvargs
        return
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

def printNames(first, last):
    pass

def main():
    
    #Demonstrates difference between global & local scope
    mainNumber = 5
    print "mainNumber equals", mainNumber, "in function main"
    scopeFunction()
    print "mainNumber equals", mainNumber, "after scopeFunction"
    print id(mainNumber)
    
    # Force a global variable to change
    print "globalVariable before changeGlobal =", globalVariable
    changeGlobal()
    print "globalVariable after changeGlobal =", globalVariable
    
    # Create a function with a docstring
    print addNumbers(1)
    print addNumbers.__doc__
    
    # Add undefined number of numbers with a tuple
    print addUndefNums(1,2,3,4,5,6,7,8)
    
    # Create a dictionary
    createDict(Name='Karram Sos', Age=40, Yearborn=1774)
    createDict(Cust1=('Singh',35,1974), Cust2=('Sukh',25, 1984),Cust3=('Alex',15,1994))
    
    # Demonstrate Recursion
    print factorial(3) 
    
'''
Demonstrate Recursion
def factorial(3):
    if 3 == 1:
        return 1
    else:
    return 3 * factorial(2)

def factorial(2):
    if 2 == 1:
        return 1
    else:
    return 2 * factorial(1)

def factorial(1):
    if 1 == 1:
        return 1

'''

if __name__ == '__main__': main()   