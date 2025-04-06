class Person:
  def __init__(self, firstname, age):
    self.name = firstname
    self.age = age

  def __str__(self):
     return (f"A new instance has been created: {self.name}({(self.age)})")

p1 = Person("John", 36)



# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return f"{self.name}({self.age})"

# p1 = Person("John", 36)