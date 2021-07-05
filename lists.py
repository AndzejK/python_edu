import _myFunction
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

list_num=[1,2,3] 
list_abc=['a','b','c']   
list_=list_num+list_abc
print(list_)
print(list_[0:3])
print(list_[3:])
print(dir(list_)) #we can find the methods which can be applied on list
_myFunction.separator() #I'm using external file where separator method lives
#append method
list_.append('d') #adds the end of the list a value
print(list_)
print(1 in list_) #if 1 is "in" the list? -True
print(4 not in list_) #if 4 is "not in" the list? -True
_myFunction.separator() 
#an AVG calc
total=0
count=0
while True:
    inp=input('Enter a number: ')
    if inp=='done':
        break
    number=float(inp)
    total+=number
    count+=1
avg=total/count
print('The average:',avg)
_myFunction.separator() 

#an AVG cacl this method uses more memory.
numList=list()
while True:
    inp=input('Enter a number: ')
    if inp=='done':
        break
    num=float(inp)
    numList.append(num)
avr=sum(numList)/len(numList)
print('The average:',avr)