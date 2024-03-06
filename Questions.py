# 1. write a program to find largest number out of three accepted from the User
# 2. write a  python program to accept age of 4 peoples and display the oldest one 
# 3. write a program to find th eamount of electricity bill on the basic of following data[take input as number of units from user]
# first 100 : free
# 200 units : 2rs/unit
# 300 units : 5rs/unit

unit = int(input("Enter The Unit : "))

if(unit<=100):
    print("Electricty Is Free")
elif(unit>100 and unit<=200):
    amount=(unit-100)*2
    print("The Amount Of Electricity Is : ",amount)
elif(unit>200 and unit<=500):
    amount=(unit-100)
    total = amount
    total = ( (total - 100) * 5 ) + 100 * 2

    print("The Amount Of Electricity Is : ",total)