# implement a simple calculator using for or while loop
print("Simple Calculator Program \n")

print("1. Addition")
print("2. Substraction")
print("3. Division")
print("4. Multiplication")
print("5. Exit")
num = int(input("Enter The Number (1-5), You Want To Perform Operation : "))

if num in [1,2,3,4]:
       numbers = int(input("Enter The Numbers You Want To Perform Operation : "))
       sum = 0
    #    num1 = int(input("Enter The First Number : "))
    #    num2 = int(input("Enter The Second Number :"))  

       if(num==1):
        for i in range(numbers):
           num1 = int(input("Enter The Numbers : "))
           sum = sum + numbers
           print("The Addition Is",sum)
elif(num==2):
        for i in range(numbers):
               num1 = int(input("Enter The Numbers : "))
               sum = sum - numbers
        print("The Addition Is",sum)
elif(num==3):
        num1 = int(input("Enter The First Number :"))
        num2 = int(input("Enter The Second Number :"))
        print("The Division Of ",num1," And ",num2," Is",num1/num2)
elif(num==4):
        for i in range(numbers):
               num1 = int(input("Enter The Numbers : "))
               sum = sum * numbers
        print("The Addition Is",sum)
elif(num==5):
    print("You Have Exited...!")
else:
        print("You Have Entered Invalid Number...!")
