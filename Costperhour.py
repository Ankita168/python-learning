#Calculating Cost per hour using try except
Hour= input("Enter hour : ")
Rate = input("Enter Rate per hour :")
try:
    Chour = int(Hour)
    CRate = int(Rate)
except:
    Chour = -1
    CRate = -1
if Chour > 0 and CRate > 0:
    Total = int(Hour) * int(Rate)
    print("Total Cost is", Total)
else:
    print("Enter valid input")