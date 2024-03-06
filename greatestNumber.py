num1 = int(input("Enter The First Number : "))
num2 = int(input("Enter The Second Number : "))
num3 = int(input("Enter The Third Number : "))

if(num1>num2 and num1>num3):
    print(num1," Is The Greatest Number")
elif(num2>num1 and num2>num3):
    print(num2," Is The Greatest Number")
else:
    print(num3," Is The Greatset Number")