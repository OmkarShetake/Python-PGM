num1= int (input("enter first value: "))
num2= int (input("enter 2nd value: "))
num3= int (input("enter 3rd value: "))
if (num1>=num2)and (num1>=num3):
    print("first value is greatest")
elif num2>num1 and num2>=num3:
    print("2nd value is greatest")
else:
    print("3rd value is greatest")