# a) Method Overriding (Runtime Polymorphism)

class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement this method")

class Dog(Animal):
    def speak(self): # overriding a speak method from Superclass of Animal
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Polymorphic behavior
animalNoSpeak=Animal()

# Error Handling case
# try:
#     animalNoSpeak.speak() # raises NotImplementedError 
# except NotImplementedError as err:
#     pass
#     print('\n',err,'\n')

# finally: 
#     print(f"Error handling was handled, and this a final (finally) statemet just for sake of learning!\n") # no need for this statement but it's good for for handling files to close the final and do clean-up after yourself

# animals = [Dog(), Cat()]
# for animal in animals:
#     print(animal.speak())  # Output: Woof! Meow!


# c) Operator Overloading = Contextual behavior!

# ## What is 'overloading'? you remain the meaining of something, in this case operator , +,-,*... and add extend to fit your customasations. Good for: #1 multiple meanings, #2 Extented functionality #3 Context-dependent behavior

# 4 Duck Typing in Python

# Principle: "If it walks like a duck and quacks like a duck, then it’s a duck."
# No Explicit Interfaces: Focus on methods/attributes an object has, not its type.

class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm pretending to be a duck!")

def make_it_quack(obj):
    obj.quack()  # Works if `obj` has a `quack()` method

# make_it_quack(Duck())   # Quack!
# make_it_quack(Person()) # I'm pretending...

# Polymorphysim ABC - Absrtact Base Classess 

from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def speak(self):
        """All animals must implement a speak method"""
        pass
        
    def move(self):
        """Default implementation that subclasses can override"""
        return "Moving..."

class Dog(Animal):
    def speak(self):
        return "Woof!"
    # a default move()

class Cat(Animal):
    def speak(self):
        return "Meow!"
    # a default move()

class Duck(Animal):
    def speak(self):
        return "Quack!"
    
    # mod move()     
    def move(self):
        return "Swimming..."

# An e.g. of a failed to obey ABC 
# class Incomplete(Animal): # A subclass does not implement SPEAK() method 
#     pass  # Missing speak() implementation

# inst_of_Incomplere_subcl=Incomplete() # TypeError: Can't instantiate abstract class Incomplete with abstract method speak

def animal_farm(animals:list) -> str:
    for animal in animals:
        print(f"The {animal.__class__.__name__} says: {animal.speak()}")
        print(f"And it's {animal.move()}")
        print()
animals=[Dog(),Cat(),Duck()] # [<__main__.Dog object at 0x102447450>, <__main__.Cat object at 0x102447490>, <__main__.Duck object at 0x1024474d0>]


