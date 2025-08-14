A= int (input("enter first value: "))
B= int (input("enter 2nd value: "))
C= int (input("enter 3rd value: "))
if (A<B)and (A<C):
    print("first value is smallest")
elif B<A and B<C:
    print("2nd value is smallest")
else:
    print("3rd value is smallest")