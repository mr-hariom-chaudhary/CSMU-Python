num = int(input("Enter The Number : "))
a = 0 
b = 1
print(num)

for i in num:
    c = a + b
    b = a
    c = b
    print(c)