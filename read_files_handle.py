def separator():
    sep='-'
    print(sep*10)
xfile=open('files_to_read/email_chat.txt')
for cheese in xfile:
    print(cheese) #we are printing each time a new line from "email_chat.txt" all to the end
separator()
#get the number of lines in the given file    
xfile=open('files_to_read/email_chat.txt')
count=0
for line in xfile:
    count+=1
print("Line count:",count)
separator()
#Reading the "whole" file
##we can read the whole file (newlines and all) into a single string
fhand=open('files_to_read/email_chat.txt')
inp=fhand.read()
print("Total words in the file:",len(inp))
print(inp[:38]) #we print/display just first 38 characters 

#Searching through a file
##In this case we are going to look for a line which starts with a word
separator()
fhand=open('files_to_read/email_chat.txt')
for line in fhand:
    if line.startswith('From:'):
        print(line) #each line ends with a \n "new line","space", therefore, in order to have a nice line we can use strip() fn

#Stripping whitespaces
separator()
fhand=open('files_to_read/email_chat.txt')
for line in fhand:
    line=line.rstrip()
    if line.startswith('From:'):
        print('Attempt #1:',line)

#Other way of find wishing result
separator()
fhand=open('files_to_read/email_chat.txt')
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From:'): #if the line does NOT start with 'FROM:' skip it
        continue
    print('Attempt #2:',line)
separator()

#Other way of find wishing result with IN operator
fhand=open('files_to_read/email_chat.txt')
for line in fhand:
    line=line.rstrip()
    if not 'From:' in line: #if 'From:' is NOT in the line skip it "continue"
        continue
    print('Attempt #3:',line)
separator()

#Using prompt to indicate a file's location
loc_name=input('Enter the file location: ')
fhand=open(loc_name)
count=0
for line in fhand:
    count+=1
print("Line count:",count)
separator()

#Expecting that file can a bad name
loc_name=input('Enter the file location: ')
try:
    fhand=open(loc_name)
except:
    print('File cannot be opened:', loc_name)
    quit() #we use quit() method to prevent code from running since our code blew up on this line and it doesn't make to continue; therefore, we stop at that line
count=0
for line in fhand:
    count+=1
print("Line count:",count)