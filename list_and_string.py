import _myFunction
sentence="If you want to convert an integer number to an uppercase or lower hexadecimal string with prefix or not, you can use either of the following ways"
list_of_word=sentence.split()
print(len(list_of_word))
print(list_of_word)
_myFunction.separator()

xfile=open('files_to_read/email_chat.txt')
for line in xfile:
    line=line.rstrip()
    if not line.startswith('From:'):
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