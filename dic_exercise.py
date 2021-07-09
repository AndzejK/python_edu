file_name=input("enter file: ")
if len(file_name)<1: #if a files is not provided take default one, intro.txt
    file_name='files_to_read/intro.txt'
handle=open(file_name)
dictn=dict()#creating an empty dictionary count words and have their keys
#read the line from the given file
for l in handle:
    l=l.rstrip()
    #print(l) #print a line
    get_words=l.split()
    #print(get_words) #find each word based on space and put it into the List
    #get_len_l=len(get_words)
    #print(get_len_l) #print the total count words in each line
    for print_word in get_words: #looping through a List/array of separated word 
        #print(print_word)
        #print('**',print_word,dictn.get(print_word,-99))
        #if print_word in dictn:
            #if the key is not there the count is zero
        #old_count=dictn.get(print_word,0)
        #print(print_word,'-old-',old_count)
            #dictn[print_word]=dictn[print_word]+1 #if the key/word is the dictionary add 1 to the value/count
        #new_count=old_count+1
        #dictn[print_word]=new_count
        #print(print_word,'-new-',new_count)
            #print('**Existing**')
        #else:
            #dictn[print_word]=1 # add a new pair in the dictionary. In this way, we check if this key/word exist already in the dictionary
            #print('**New**')
        #print(print_word,dictn[print_word]) #print each time a new word and when you are done come back the 1st FOR loop

        #2simple way of counting words using get() method
        dictn[print_word]=dictn.get(print_word,0)+1
print(dictn)

#Find the most commnon word
largest=-1
the_common_word=None
for k,v in dictn.items():
    if v>largest:
        largest=v
        the_common_word=k #capture/remeber the that was largest
print("the most common word:",the_common_word,'repeated:',largest)