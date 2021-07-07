import _myFunction
name=input('Enter file:')
handle=open(name)

#simple couting each character which as seperated by "space"
counts=dict()
for line in handle:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1
print(counts)
_myFunction.separator()
#/Users/mac/Documents/coding/python/edu/files_to_read/bbc_article.txt

#finding the most usable word
bigcount=None
bigword=None
for word,count in counts.items(): #special feature in python, where can loop through key and value 
    if bigcount is None or count>bigcount: #remember number, what count is the largest
        bigword=word
        bigcount=count
print(bigword,bigcount)