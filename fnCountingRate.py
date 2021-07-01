def caclpay(hours,rate):
    print("hours:",hours,"rate:",rate)
    if hours>40:
        overTimePay=(hours-40)*(rate*1.5)
        pay=overTimePay+(40*rate)
    else:
        pay=hours*rate
    return pay #we need to indicate that we want to return some value

sh=input("Enter hours: ")
sr=input("Entrer Rate: ")
fh=float(sh)
fr=float(sr)

finalPay=caclpay(fh,fr)
print("The pay is:",finalPay)