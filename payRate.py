#checkind on numeric data at the begining of the code;
try:
    hours=input("Please enter your hours: ");
    intHour=int(hours)
    rate=input("What is your rate: ");
    intRate=int(rate)
#above 40 hours rate increases by 1.5;
except:
    print("error, please enter numeric input")
    quit() #stop below code from running;

if int(hours)>40:
    overtimepay=(intHour-40)*(intRate*1.5)
    pay=overtimepay+(40*intRate)
    print("overtime:",overtimepay)
else:
    pay=intHour*intRate;

print("Your pay is:",float(pay))