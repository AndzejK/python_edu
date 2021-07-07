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

#to count how many items/names in the list (Counting)
counts=dict()
names=["Andrey","Mark","Pavel","Brodie","Andrey"]
for name in names:
    if name not in counts:
        counts[name]=1
    else:
        counts[name]=counts[name]+1
print(counts)
counts={}
_myFunction.separator()
#.get() method does the same as the lines 16, 17, 18, 19 (Counting)
for name in names:
    counts[name]=counts.get(name,0)+1
print(counts)
_myFunction.separator()
#The syntex would be if the following key exists in the dictionary if not will print default value; 
print(counts.get("Catie",'Nope she is not interesting in you')) 