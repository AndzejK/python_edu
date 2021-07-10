file_name=input('Enter file: ')
file_handle=open(file_name)
counts=dict()#new dictionary for words and their counts
for line in file_handle: #loop through each line in the file
    line=line.rstrip()#remove space from right side
    words=line.split()#separate each word based on space and put it into a list
#create dictionary where we have the count of the words
    for word in words:#loop through each word in the list
        counts[word]=counts.get(word,0)+1 #for the first time we adding new pairs into dictionary and the key exists already add one to its value
#create a list and add a tulpe 
lst=list()
for key,val in counts.items():#put key and value of the dictionary into a list
    newtup=(val,key)#we reverse values in order to sort number based on the key
    lst.append(newtup)#add a tulp to the list

lst=sorted(lst,reverse=True) #sort the list in descending order
#give 10 first tulpes in the list
for val,key in lst[:10]:
    print(key,val)

