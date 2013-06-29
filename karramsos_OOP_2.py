#! /usr/bin/python

# About this snippet: An Object Oriented Programming example
# Author: Sukhvinder Singh | karramsos@gmail.com | @karramsos

__metaclass__ = type

class Animal:
    
    __name = "No Name"
    __owner = "No Owner"
    
    def __init__(self, **kvargs): # The constructor function called when object is created
        self._attributes = kvargs
    
    # There is a function called a destructor __del__, but its best to avoid it
    def set_attributes(self, key, value): # Accessor Method
        self._attributes[key] = value
        return
    
    def get_attributes(self, key):
        return self._attributes.get(key, None)
    
    def noise(self): # self is a reference to the object
        print('errr') # You use self so you can access attributes of the object
        return
    
    def move(self):
        print('The animal moves forward')
        return
    
    def eat(self):
        print('Crunch, crunch')
        return
    
    def __hiddenMethod(self): # A hidden method
        print "Hard to Find"
        return

class Dog(Animal):
    
    def __init__(self, **kvargs): # Not needed unless you plan to override the super
        super(Dog,self).__init__()# This wouldn't work without the second line
        self._attributes = kvargs
    
    def noise(self): # Overriding the Animal noise function
        print('Woof, woof')
        Animal.noise(self)
        return

class Cat(Animal):
    
    def __init__(self, **kvargs):
        super(Cat,self).__init__()
        self._attributes = kvargs
        
    def noise(self):
        print('Meow')
        return
    
    def noise2(self):
        print('Purrrr')
        return
    
class Dat(Cat, Dog):
    
    def __init__(self, **kvargs): # Not needed unless you plan to override the super
        super(Dat, self).__init__()
        self._attributes = kvargs
        
    def move(self):
        print('Chases Tail')
        return

def playWithAnimal(Animal): #This is polymorphism
    Animal.noise()
    Animal.eat() # Works even if the method isn't in Cat because Cat is an Animal
    Animal.move()
    print(Animal.get_attributes('__name'))
    print(Animal.get_attributes('__owner'))
    print'\n'
    Animal.set_attributes('clean', 'Yes')
    print(Animal.get_attributes('clean'))
    
jake = Dog(__name='Jake', __owner = 'Paul')
sophie = Cat(__name = 'Sophie', __owner = 'Sue')
playWithAnimal(sophie)
playWithAnimal(jake)

# print sophie.__hiddenMethod() Demonstrating private methods

print issubclass(Cat, Animal) # Check if Cat is a subclass of Animal
print Cat.__bases__           # Prints out the base class of a class
print sophie.__class__        # Prints the objects class
print sophie.__dict__         # Prints all of an objects attributes

japhie = Dat(__name = 'Japhie', __owner = 'Sue' )
japhie.move()
print japhie.get_attributes('__name')
    
        