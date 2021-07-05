import _myFunction
sentence="If you want to convert an integer number to an uppercase or lower hexadecimal string with prefix or not, you can use either of the following ways"
list_of_word=sentence.split()
print(len(list_of_word))
print(list_of_word)
_myFunction.separator()

xfile=open('files_to_read/email_chat.txt')
for line in xfile:
    line=line.rstrip()
    if not line.startswith('From:'): #if it's true (I can't find 'From:' come back to the start of the loop)
        continue
    words=line.split()
    email=words[3]
    pieces=email.split('@')
    domain=pieces[1]
    name=pieces[0]
    correct_domain=domain.replace(">",'')
    correct_name=name.replace('<','')
    print(correct_domain)
    print(correct_name)
_myFunction.separator()

xfile=open('files_to_read/email_chat.txt')
count=0
for line_w_ARC in xfile:
    line_w_ARC=line_w_ARC.rstrip()
    if not line_w_ARC.startswith('ARC'): #we're ignoring the lines which are not starting with "ARC"
        continue #continue statement is used to skip further instruction in the loop for that iteration
    print(line_w_ARC) #when we find the line which starts with "ARC", we are printing them