# print(f"\nmymodule __name__: {__name__}\n")

# def say_my_name(name):
#     print(f"Your name is:{name}")


def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

if __name__ == "__main__":
    print(add(2, 3))  # Test code
else:
    print(f"\n","-"*10,{__name__},"-"*10)

    # A seperate file with code that contains functions, variables which can be used by my code.

# Built-in modules 
import platform #,sys,os
x = platform.system()
# print(__name__)

# print(dir(platform))
# print(sys.path)
# print(f"The __name__ is: {__name__}")

# module_dir= os.path.dirname(__file__)
# print(module_dir)
# print(sys.__doc__)
