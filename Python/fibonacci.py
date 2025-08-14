num = int(input("Enter number of terms: "))  
a, b = 0, 1
count = 0
while count < num:
    print(a)
    a, b = b, a + b               
    count += 1