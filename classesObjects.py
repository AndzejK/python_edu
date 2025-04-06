class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
     return (f"A new instance has been created: {self.name}({(self.age)})")

  # method that will belog to an obj
  def my_fn(self):
    print(f"Hey there, my name is {self.name}")

p1 = Person("John", 36)
print(p1)
print(p1.name)
print(p1.my_fn)
p1.my_fn()
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return f"{self.name}({self.age})"

# p1 = Person("John", 36)