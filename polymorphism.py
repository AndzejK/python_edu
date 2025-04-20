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
try:
    animalNoSpeak.speak() # raises NotImplementedError 
except NotImplementedError as err:
    print('\n',err,'\n')

finally: 
    print(f"Error handling was handled, and this a final (finally) statemet just for sake of learning!\n") # no need for this statement but it's good for for handling files to close the final and do clean-up after yourself

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())  # Output: Woof! Meow!


# c) Operator Overloading = Contextual behavior!

# ## What is 'overloading'? you remain the meaining of something, in this case operator , +,-,*... and add extend to fit your customasations. Good for: #1 multiple meanings, #2 Extented functionality #3 Context-dependent behavior

