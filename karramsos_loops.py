#! /usr/bin/python

# About this snippet: Examples on loops
# Author: Sukhvinder Singh | karramsos@gmail.com | @karramsos

listEx = [4,5,6]

stringEx = 'Random String'

print 3 in listEx

print 'String' in stringEx

# While Loops

x = 1

while x <= 30:
    print x
    x += 1

# for loops

listCustNum = [0,1,2]
listCustName = ['Bob Smith', 'Helen Jones', 'Mark Summers']
listCustAge = [23,70,45]

for i in listCustNum:
    print '%s is %d' % (listCustName[i], listCustAge[i])

listEx = [1,2,3,4]

print 2 in listEx

for i in listEx:
    print i
    
listEx[:] = range(1,31)

for i in listEx:
    print i

# Print just odd numbers

for i in listEx:
    if(i%2) == 0:
        continue
    else:
        print i

# Print odd numbers up till 25

for i in listEx:
    if(i%2) == 0:
        continue
    elif i == 25:
        break
    else:
        print i,