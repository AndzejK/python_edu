# Base/Superclass
class A:
    def method(self):
        print("A.method()")

# Derived/subclass
class B(A):
    def method(self):
        print("B.method()") 
class C(B):
    pass

c = C() # object 'c' inhertis data from class B and class inherits from class A
# c.method()
# print(C.mro()) 
#  The order of class lookup: C, B, A                               # the base class
# [<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

b = B()

# b.method()
# print(B.__mro__)

class A1:
    def method(self):
        print("A1.method()")

class B1:
    def method(self):
        print("B1.method()")

class C1(B1, A1):
    pass

c1=C1()
# print(C1.mro())

    # if class C1(A1, B1) then  MRO: C, B, A
# [<class '__main__.C1'>, <class '__main__.A1'>, <class '__main__.B1'>, <class 'object'>]

    # if class C1(B1, A1) then MRO: C, B, A
# [<class '__main__.C1'>, <class '__main__.B1'>, <class '__main__.A1'>, <class 'object'>]


######### START: Example No.02 #########

class X:
    pass

class Y:
    pass

class A(X, Y):
    pass

class B(X, Y):
    pass

# This would cause an error because it creates an impossible linearization
class C(A, B):
    pass

# This works because it maintains consistent ordering
class D(B, A):
    pass

# print(A.__mro__)
# (<class '__main__.A'>, <class '__main__.X'>, <class '__main__.Y'>, <class 'object'>)

# print(B.__mro__)
# (<class '__main__.B'>, <class '__main__.X'>, <class '__main__.Y'>, <class 'object'>)

# print(C.__mro__)
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.X'>, <class '__main__.Y'>, <class 'object'>)

# print(D.__mro__) 
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.X'>, <class '__main__.Y'>, <class 'object'>)

######### END: Example No.02 #########

######### START: E.X W3S #########

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

agent_001=Person("John", "Smith")
# agent_001.printname()

# Derived class
class Student(Person):
    def __init__(self,fname,lname,age): # contructor overriding
        self.stdudent_age=age
        Person.__init__(self, fname, lname) # direct parent class reference 
    
    def print_age(self):
        print(f"{self.firstname} is {self.stdudent_age} years old.")

# agent_002=Student("Andrew", "Collen",23)
# agent_002.printname()
# agent_002.print_age()

######### END: E.X W3S #########

######## START: Questions based on Inheritance ########

"""
1. What happens when a derived class calls super().__init__()?
C) It calls the constructor of the next class in the Method Resolution Order (MRO)

2. In Python, what is the main difference between calling Parent.__init__(self, ...) and super().__init__(...)?
B) super() follows the MRO while direct class reference doesn't

3. Which statement about Python's multiple inheritance is TRUE?
C) Method resolution in multiple inheritance follows the C3 linearization algorithm

4. What is the primary purpose of the Method Resolution Order (MRO) in Python?
B) To determine the order in which methods should be looked up in inheritance hierarchies

5. If a method is defined in both a parent class and a child class, which version will be called when the method is invoked on a child class instance?
B) The child class version

"""

class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B" + super().method()

class C(A):
    def method(self):
        return "C" + super().method()

class D(B, C):
    def method(self):
        return "D" + super().method()

"""
6. What will D().method() return? 
C) "DBCA"

7. What is the MRO of class D?
B) [D, B, C, A, object]
"""

######## END:   Questions based on Inheritance ########

######## START: super() function e.x ########

'''super() function is a grat choice especially for multiple inheritance and it followes the MRO
Based on the question 6, line 146, we can see that all methods were inherited, super()  is used'''

class Animal:
    def __init__(self,name):
        self.animal_name=name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name) # 1st I want inherit all atrributes from Animal calls, common attributes
        self.dog_breed=breed # adding one more specific attribute to Dog class
    
    def speak(self):
        return f"{self.animal_name} says Woof!, I'm a {self.dog_breed}"

mayor = Dog('Mayor','rottweiler')

######## END:   super() function e.x ########

######## START: Simple Logging ########

'''
Write a class MixinLogger that provides a logging functionality. 
Then create
a class User and 
a class LoggedUser 
that inherits from both User and MixinLogger.
'''

class MixinLogger:
    def log(self,msg):
        print(f"LOG_INFO: {msg}")

# create a suer
class User:
    def __ini__(self,name):
        self.username=name
    
    def greet(self):
        return f"Hey, {self.username}"

class LoggedUser(User,MixinLogger):
    def __init__(self, name):
        super().__init__(self, name)
        self.log(f"Created user {name}")
    
    def greet(self):
        msg=super().greet()
        self.log(f"User {self.username} was greeted.")
        return msg

rock=User("rock")
print(rock)

######## END: Simple Logging ########