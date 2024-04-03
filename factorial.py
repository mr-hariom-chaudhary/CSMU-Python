num = int(input("Enter The Number You Want To Find Factorial of : "))
fact = 1
for i in range(1,num+1):
    fact = fact * i
print(fact)