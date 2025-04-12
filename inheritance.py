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
agent_001.printname()

# Derived class
class Student(Person):
    def __init__(self,fname,lname,age):
        self.stdudent_age=age
        Person.__init__(self, fname, lname)
    
    def print_age(self):
        print(f"{self.firstname} is {self.stdudent_age} years old.")

agent_002=Student("Andrew", "Collen",23)
agent_002.printname()
agent_002.print_age()

######### END: E.X W3S #########