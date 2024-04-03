import random

lower = int(input("Enter The Lower Bond : "))
upper = int(input("Enter The Upper Bond : "))
r_Num = random.randint(lower,upper)

num = int(input("Guess The Number : "))

guess = 0
count=1

while num != r_Num:
    if num>r_Num:
        print("Enter Lower Number !")
    
    elif num<r_Num:
        print("Enter Higher Number !")
    
    else:
        print("You Have Guessed The Number..!",r_Num)