# Importing Random Library
import random

# Input Lower Bond & Upper Bond
lower = int(input("Enter The Lower Bond : "))
upper = int(input("Enter The Upper Bond : "))

# Generating Random Number From Lower & Upper Bond
x = random.randint(lower,upper)

# Initalizing count to 0
count = 0

# Creating Loop for Guessing Chances
while count < 5:
    count+=1
    # Input The Guess Number
    guess = int(input("Guess The Number : "))

    if x==guess:
        print("You Have Guessed The Number In : ",count,"Chances.")
        break
    elif x > guess:
        print("Your Guess Is Lower...Try to Guess Higher Number..!")
    elif x < guess:
        print("You Guess Is Higher...Try to Guess Lower Number..!")

if count == 5:
    print("The Number Was : ",x)
    print("You Failed to Guess That Number..!")
    print("Better Luck Next Time...!")