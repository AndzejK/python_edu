#Indefinite loops
n=0
while True:
    if n==10:
        break #we're telling to the "while loop" stop executing entire loop
    print(n)
    n=n+1
print("")

#Definite loops
friends=["Brodie","Max","Chris"]
for friend in friends:
    print("Have a good one:", friend)
print("Hopefully, I haven't missed anyone!\n")

#Loop idioms
#1. Finding the largest value
set_of_numbers=[9,12,3,47,5,90,2,89]
largest_so_far=-1
print("Before",largest_so_far)
for the_num in set_of_numbers:
    if the_num>largest_so_far:
        largest_so_far=the_num
    print(largest_so_far,the_num)
print("After",largest_so_far)

#2. Finding the smallest value
set_of_numbers=[9,12,3,47,5,-1,90,2,89,0]
smallest_so_far=set_of_numbers[0] #Take the 1st number from the array and assume it's the smallest number;
print("1st number from the array: ", smallest_so_far) 
for the_num in set_of_numbers:
    if the_num<smallest_so_far:
        smallest_so_far=the_num
    print(smallest_so_far,the_num)
print("the smallest number is: ", smallest_so_far)

# None is a special type of data just one value NONE
print(None is -1)
# "is" and "is not" are operators and they return boolean value True of False
# "is" the same as "==", "is not" as "!="

#2.1 Finding the smallest value using None value
smallest_so_far_none=None
for i in set_of_numbers:
    if smallest_so_far_none == None: #it will be executed just once during this loop
        smallest_so_far_none=i
    elif i<smallest_so_far_none:
        smallest_so_far_none=i
    print(smallest_so_far_none,i)
print("the smallest number is: ", smallest_so_far_none)