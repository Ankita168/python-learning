Value1 = input("Enter a number:")
try:
    check = int(Value1)
except:
    check = -1
if check > 0:
    print("Nice work")
else:
    print("Not a number")