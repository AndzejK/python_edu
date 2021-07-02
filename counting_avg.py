# Write a program which repeadly reads numbers untill the user enters "done". Once "done" is entered,
# print out the total, count and average of the numbers. If the user enters other than a number, detect
# their mistake using "try"&"except" and print an error message and skip to the next number

# TO COMMENT MULTIPLE LINES cmd+/ COMBINATION

# total=0
# count=0
# usrs_number=None
# while(usrs_number!="done"):
#     try:
#         usrs_number=input("Enter a number: ")
#         int_usrs_number=int(usrs_number)
#     except:
#             print("Invalid input")
#             continue # "continue" indicates to come back to line 8 (to the beginning of the loop)
#     if(int_usrs_number):
#         count+=1
#         total+=int_usrs_number
# print("Total:",total,"Attempts:",count,"The avg",total/count)

# Solution from the video
count=0
tot=0
while True:
    strvalue=input('Enter a number: ')
    if strvalue=='done':
        break
    try:
        intvalue=int(strvalue)
    except:
        print('Invalid input')
        continue
    count+=1
    tot+=intvalue
print(tot,count,tot/count)