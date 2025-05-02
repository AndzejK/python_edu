global_var="I am defined in the main body"
def outer_fn():
    inner_var="outer\n"
    global_var="not anymore global var"
    print(inner_var,global_var)

    def outer():
        print(inner_var)
        print(global_var)

    outer()

# inner_var="outside"
# outer_fn()
# print(global_var)

# Keywords: nonlocal 

def main_fn():
    x="I am defined in a main fn"
    print(x)
    def nested_fn():
        # print(x) SyntaxError: name 'x' is used prior to nonlocal declaration
        nonlocal x
        x = "I changed the value while being inside the main fn using a keyword NONLOCAL"
        print(x)
    nested_fn()
    return x

# print(main_fn())

# Closure 
def outer():
    msg="outer"
    def inner():
        print("I am nested")
        print(msg)
    return inner

# main_fn=outer()
# print("pause/code")
# main_fn()

funtions=[]

for i in range(3): # 0,1,2 # 0
    def fn(arg=i): # !!! asign the the current value otherwise each fn will have a final value
        print(arg) # 0
    funtions.append(fn)

# for fn in funtions:
#     fn()

# Option No.2 using lambda fn to capture the cur value!
fns=[]
for i in range(3):
    fns.append(lambda i=i:print(i))

# for fn in fns:
#     fn()

# Shadowing 

global_value=10

def demo():
    global_value=20
    local_val=global_value
    print(local_val)
# demo()

# print(global_value)

# Nested Scope Shadowing (Hidding)
def outer():
    x="outer"

    def inner():
        x="inner" # Hides/Shadows outer's x value
        print(f"Inner x: {x}")
    
    inner()
    print(f"Outer x: {x}")
outer()

