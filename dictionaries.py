import _myFunction
myDic=dict() #creating a new empty dictionary
print(myDic)
_myFunction.separator()
other_dic={'key':'value', 0:"Andrej", "age":30} #Dictionary literals
print(other_dic)
age=other_dic["age"]
_myFunction.separator()
print(age)
_myFunction.separator()

#to count how many items/names in the list
counts=dict()
names=["Andrey","Mark","Pavel","Brodie","Andrey"]
for name in names:
    if name not in counts:
        counts[name]=1
    else:
        counts[name]=counts[name]+1
print(counts)
    