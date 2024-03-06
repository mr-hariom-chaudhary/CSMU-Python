age1 = int(input("Enter The First Age : "))
age2 = int(input("Enter The Second Age : "))
age3 = int(input("Enter The Third Age : "))
age4 = int(input("Enter The Fourth Age : "))

if(age1>age2 and age1>age3 and age1>age4):
    print(age1," Is The Greatest Age")
elif(age2>age1 and age2>age3 and age2>age4):
    print(age2," Is The Greatest Age")
elif(age3>age1 and age3>age2 and age3>age4):
    print(age3," Is The Greatest Age")
else:
    print(age4," Is The Greatest Age")