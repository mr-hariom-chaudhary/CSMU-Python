print("-----------------------------------------------------------------------------------------------------------------------------------------\n")
print("Simple Calculator Program\n")

print("1. Addition")
print("2. Subtraction")
print("3. Division")
print("4. Multiplication")
print("5. Exit")

num = int(input("Enter The Number (1-5) For The Operation You Want To Perform : "))

if num in [1, 2, 3, 4]:
    numbers = int(input("Enter The Total Numbers You Want To Operate On: "))
    result = 0

    if num == 1:
        for x in range(numbers):
            num1 = int(input("Enter A Number: "))
            result = result + num1
        print("The Sum is", result)

    elif num == 2:
        num1 = int(input("Enter A Number : "))
        result = num1
        for x in range(1, numbers):
            num1 = int(input("Enter A Number: "))
            result = result - num1
        print("The Substraction is", result)

    elif num == 3:
        num1 = float(input("Enter The Numerator : "))
        num2 = float(input("Enter The Denominator : "))
        if num2 != 0:
            print("The Division Is : ", num1 / num2)
        else:
            print("Error: Division By Zero!")

    elif num == 4:
        result = 1
        for x in range(numbers):
            num1 = int(input("Enter A Number: "))
            result = result * num1
        print("The Product is", result)

    else:
        print("Invalid input! Please enter a number between 1 and 5.")

elif num == 5:
    print("Exiting the program...")
else:
    print("Invalid input! Please enter a number between 1 and 5.")
