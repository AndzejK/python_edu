def separator():
    sep='-'
    print(sep*10)

#Looping through Strings
##One of the ways of looping through strings
fruit='mango'
index=0
while index<len(fruit):
    letter=fruit[index] #we can fetch the index itself using while loop, FOR, not
    print(index,letter)
    index+=1
separator()
##A determinant way of looping through "FOR" it's more elegant way
for letter in fruit:
    print(letter)
separator()
# Slicing  Strings
## s[x:y]- up to but not including, start at "x" but not include "y"
### the "in" keyword can also be used as an operator to check to see if one string is "in" another string
### the "in" expression is a logical expression that returns True or False, can be used in an "if" statement

quote="We should remember that even Nature’s inadvertence has its own charm, its own attractiveness."
word_from_quote_uppercase=quote[10:18].upper() #returns new value
print(word_from_quote_uppercase)

#Search and Replace
quote_mod=quote.replace('should','will')
word_from_quote_mod_uppercase=quote_mod[3:7].upper()
print(word_from_quote_mod_uppercase)
separator()
#Whitespace 
## "lstrip()" - removes whitespace at the left
## "rstrip()" - removes whitespace at the right
## "strip()" - removes both begining and ending whitespace

#Parsing and Extracting
extract_from_email="From smtp.mailfrom=olga.romanova@informationplanet.com.au some random noise"
##Let's find the domain of email address 
findat=extract_from_email.find('@') #find the index of "@", the beginning of domain address
#print(findat)
findspace=extract_from_email.find(' ',findat) #find the 1st index of space after @ 
#print(findspace)
domain=extract_from_email[findat+1:findspace] 
print('E-mail domain:',domain)
