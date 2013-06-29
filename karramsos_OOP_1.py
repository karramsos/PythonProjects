#! /usr/bin/python

# About this snippet: Simple Example on Object Oriented Programming
# Author: Sukhvinder Singh | karramsos@gmail.com | @karramsos

class Animal:

    __hungry = 'Yes'
    __name = 'No Name'
    __owner = 'No Owner'

    def __init__(self):
        pass
    
    def set_owner(self, newOwner):
        self.__owner = newOwner
        return
    
    def get_owner(self):
        return self.__owner
    
    def set_name(self, newName):
        self.__owner = newName
        return
    
    def get_name(self):
        return self.__name
    
    def noise(self):
        print('errr')
        self.__hiddenmethod()
        return
    
    def __hiddenmethod(self):
        print ('Hard to find')
        return

def main():
    dog = Animal()

    dog.set_owner('Sue')
    print dog.get_owner()

    dog.noise()

if __name__ == '__main__': main()

'''
class Animal:
    
    hungary = 'Yes'
    __furry = 'Yes'
    __name = 'No Name'
    __owner = 'No Owner'
    
    def __init__(self): # The constructor function called when object is created
        __name= 'No Name'
        __owner = 'No Owner'
    
 There is a function called a destructor __de__, but its best to avoid it

    def set_owner(self, newOwner): # Accessor Method
        self.__owner = newOwner
        return

    def get_owner(self):
        return self.__owner

    def set_name(self, newName): # Accessor Method
        self.__name = newName
        return

    def get_name(self):
        return self.__name

    def noise(self): # self is a reference to the object
        print('errr') # You use self so you can access attributes of the object
        return

    def move(self):
        print('The animal moves forward')
        print Animal:__hiddenMethod(self) A Private method
        return
    
    def eat(self):
        print('Crunch, crunch')
        return
    
    def furr(self):
        print self.__furry

def main():
    dog = Animal()
    
    dog.set_owner('Sue')
    dog.set_name('Jake')
    
    print dog.get_owner()
    print dog.get_name()
    
    if dog.hungary:
        dog.eat()
    else:
        dog.move()
    
    dog.noise()
    dog.furr()

if __name__ == '__main__': main()
'''
    