#!/usr/bin/python

# Example of using dicts
# Author: Sukhvinder Singh | karramsos@gmail.com | @karramsos

dictEx = ({"Age": 35, "Height":"6'3", "Weight":165})

print dictEx

print dictEx.get("Height")

print dictEx.items()

print dictEx.values()

print dictEx.keys()

dictEx.pop("Height")

print dictEx

import math

#Formatting output with the print function
strName = 'Bob'
floatAge = 35.4
charSex = 'M'
intKids = 2
boolMarried = True

print '%s is %f years old' % (strName, floatAge)
print 'Sex: %c' % (charSex)
print 'He has %d kids and sait it\'s %s he is married' % (intKids, boolMarried)

print '%s is %.1f years old' % (strName, floatAge)

#Formatting Output Further
print '%.15f' %(math.pi)
print '%20f' %(math.pi)
print '%20.15f' %(math.pi)
print '%-25.15f is the value of pi' %(math.pi)

precisionPi = int(raw_input("How precise should pi be:"))
print 'PI = %.*f' % (precisionPi, math.pi)

# A bunch of String Methods

bigString = 'Here is a long string that I will be messing with'

print bigString[1:20:2]

print bigString.find('string')
print bigString.find('massive')

print bigString.count('e')
print bigString.count('e', 4)
print bigString.count('e', 0, 20)

copyStr = tuple(bigString)
print copyStr
print ".".join(copyStr)
print ','.join(copyStr)

print bigString.lower()
print bigString.upper()

print bigString.replace('long', 'small')

print bigString.split(' ')

randomWhite = '     This string has random white space     '
print randomWhite.strip()

