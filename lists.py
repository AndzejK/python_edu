#Algorithms - a set of rules or steps used to solve a problem
#Data Structure - a particular/"clever" way of organising data in a computer

#A collection allows us to put many values in a single "variable" - List=[x,y,z]
#FOR loop is a great way of iterating through a list 
#A list has the positions and it's 0 based List starts with rom 0
#The lists are mutable, can be changed opposite to string which is immutable

#In order to loop through indices we can use the following method
friends=["Max","Catie","Sarah"]
for index in range(len(friends)): #here we get the indixes
    friend=friends[index]
    print(index,friend)