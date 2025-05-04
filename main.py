# Fisrt Python program from PYTHON PROGRAMMING 

# defintion of the function what it SHOULD perform when it'll be exec
"""
Memory before:
x (name) → [0.5] (object)

Memory after: 
x (name) → [0.975] (object)
[0.5] (unreferenced, will be garbage collected)
"""
def main():
    print("A chaotic function")
    x = eval(input("Enter a number between 0 and 1: ")) # evaluates that string as a Python expression.
    y = eval(input("Enter a 2nd number between 0 and 1: "))
    n = eval(input("How many numbers should I print? "))
    print (f"Input\t{x}\t\t{y}\n{'-'*32}")
    for num in range(n):
        # general form: k(x)(1-x).26
        x = 3.9 * x - 3.9 * x *x #3.9 * (x-x*x)#3.9 * x  * (1-x) # 1: 0.73125, 2: 0.76644140625
        y = 3.9 * (y-y*y)
        # print(f"computed value of x = {x} its MEM address: {id(x)}")
        print(f"{' '*5}\t{x:.6f}\t{y:.6f}")
main()

def prog_exer_No_1():
    print("Hello, world!")
    print("Hello", "world!")
    print(3)
    print(3.0)
    print(2+3)
    print(2.0+3.0)
    print("2"+"3")
    print("2+3",2+3)
    print(2*3)
    print(2**3)
    print(7/3)
    print(7//2)

# prog_exer_No_1()
