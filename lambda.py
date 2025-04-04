# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

#           Syntax
#   lambda arguments : expression
x = lambda a : a + 10 # defining the lambda fn


numbers=[i for i in range(0,21)]
squared_numbers = list(map((lambda num : num**2),numbers))
even_numbers = list(map((lambda num: num if num%2==0 else 1),numbers))
# for num in numbers:
#     anonym_short_fn=lambda x : "even" if x%2==0 else "odd"
#     print(f"{num} -> {anonym_short_fn(num)}")

# Closures: Lambdas can capture variables from their enclosing scope
def make_multiplier(num):
    return lambda x: x*num

doubler=make_multiplier(2) # Created a fn that multiplies a given number by 2 and returns the result.
print(doubler(2))

# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number: