# implement a simple calculator using for or while loop
print("Simple Calculator Program \n")

print("1. Addition")
print("2. Substraction")
print("3. Division")
print("4. Multiplication")
print("5. Exit")
num = int(input("Enter The Number (1-5), You Want To Perform Operation : "))

while(num==1):
   num1 = int(input("Enter The First Number : "))
   num2 = int(input("Enter The Second Number : "))
   print("The Addition Of ",num1," And ",num2," Is",num1+num2)
   break
while(num==2):
   num1 = int(input("Enter The First Number : "))
   num2 = int(input("Enter The Second Number : "))
   print("The Substraction Of ",num1," And ",num2," Is",num1-num2)
   break
while(num==3):
   num1 = int(input("Enter The First Number : "))
   num2 = int(input("Enter The Second Number : "))
   print("The Division Of ",num1," And ",num2," Is",num1/num2)
   break
while(num==4):
   num1 = int(input("Enter The First Number : "))
   num2 = int(input("Enter The Second Number : "))
   print("The Multiplication Of ",num1," And ",num2," Is",num1*num2)
   break
while(num==5):
   print("You Have Exited...!")
   break
while(num<=0 or num>=6):
   print("You Have Entered Invalid Number...!")
   break