import _myFunction
#tuples function like a list they use brackets () they are IMMUTABLE opposite to list, we can't modify a tuple
##tuples like limited list and more efficient
###tuples are comparable
a_tuple=(1,2,3)
first_item=a_tuple[1]
print(first_item)
_myFunction.separator()
#Tuples and Dictionaries
dictn=dict()
dictn['Andrey']=7
dictn['Mike']=8
for (k,v) in dictn.items():
    print(k,v)
_myFunction.separator()
tups=dictn.items()
print(tups) #dict_items([('Andrey', 7), ('Mike', 8)])
_myFunction.separator()

dic_c={'a':10,'b':30,'c':20}
tmp=list()
for k,v in dic_c.items():
    tmp.append((v,k)) #adding tulpes into list and swapping key and values orders
print(tmp)
tmp=sorted(tmp,reverse=True) #sorted in descending order
print(tmp)
_myFunction.separator()