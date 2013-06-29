#!/usr/bin/python

# Author Sukhvinder Singh | karramsos@gmail.com | @karramsos

tupleEx = ('Derek', 35, 'Pittsburgh', 'PA') #Creating a Python Tuple

for i in tupleEx: #Cycling through all the values in the Tuple and printing them to screen
    print(i)

print("First element in the tuple is ", tupleEx[0])

smTuple = (66,)
print smTuple

tupleFunc = tuple('abcde')
print tupleFunc

#That's it tuples don't have methods

listEx = ['Derek', 35, 'Pittsburgh', 'PA']

for i in listEx:
    print(i)

# Slicing up Lists

print listEx[0:2] # Prints out the values starting at index 0 but not including the value at index 2
print listEx[-1] # Prints the last value in the List
listNum = [1,2,3,4,5,6,7,8,9,10]
print listNum[-3:] # Prints the last 3 values in the List
print listNum[:3] # Prints the first 3 values in the List

# Prints out the values starting at the first index to but not up to index 10 while skipping every other value
print listNum[1:10:2]
print len(listNum) # Prints the number of values in the List
print min(listNum) # Prints the smallest value in the List
print max(listNum) # Prints the largest value in the List

listName = list('Fred') # Creates a list with the letters F r e and d in it
print listName
listName[4:] = list('dy') # Adds the letters d and y to the list
print listName
print ''.join(listName)

listEx3 = [1,2,3,4]
listEx3[1] = 5 # Assigns the value 5 to the second index in the list
print listEx3
del listEx3[1] # Deletes the second value from the list
print listEx3

# List Methods

listEx.append("Joy") # Adds the string Joy to the end of the List

print(listEx)
print(listEx[4])

listEx.remove("Joy") # Removes the first value that is equal to "Joy" from the List

print(listEx)

listEx.remove(listEx[3]) # Removes the 4th indexed value in the List
print(listEx)

listEx.insert(2, 'PA') # Inserts 'PA' into the List at the second index position

print(listEx)

listEx2 = ['f','e','c','d','a','b']
listEx2.sort() # Sorts List alphabetically

print(listEx2)

listEx2.reverse() # Sorts list in reverse alphabetical order

print(listEx2)

# Create a multi-dimension List

listEx3 = [
    ['a','b','c'],
    ['d','e','f'],
    ['g','h','i'],
        ]

print(listEx3[2][1])

# Dictionary Example Code

dictEx = ({"Age":35, "Height":"6'3", "Weight":169}) #Creates a Python Dictionary

print(dictEx)

print(dictEx.get("Height")) # Prints the value stord with the key 'Height'
print(dictEx.items()) # Prints out all keys and values in the Dictionary
print(dictEx.values()) # Prints out just the values in the Dictionary
dictEx.pop("Height") # Deletes the key and value, where the key equals 'Height'

print(dictEx)







