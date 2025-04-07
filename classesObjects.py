class Person:
  # self - Reference to the instance of the Person class. Used to access instance variables and methods. The parameter name could be different, but 'self' is conventional in Python.
  def __init__(self, name, age):
    self.firstname = name
    self.age = age

  def __str__(self):
     return (f"A new instance has been created: {self.firstname}({(self.age)})")

  # method that will belog to an obj
  def my_fn(self):
    print(f"Hey there, my name is {self.firstname} and I'm {self.age} years old.")

p1 = Person("John", 36)

p1.age=34
print(p1.firstname)
print(p1.my_fn)
p1.my_fn()
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return f"{self.name}({self.age})"

# p1 = Person("John", 36)