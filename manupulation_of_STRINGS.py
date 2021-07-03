#Looping through Strings
##One of the ways of looping through strings
fruit='mango'
index=0
while index<len(fruit):
    letter=fruit[index] #we can fetch the index itself using while loop, FOR, not
    print(index,letter)
    index+=1
print('----')
##A determinant way of looping through "FOR" it's more elegant way
for letter in fruit:
    print(letter)
print('----')
