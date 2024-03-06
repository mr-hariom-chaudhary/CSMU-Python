unit = int(input("Enter The Unit : "))

if(unit<=100):
    amount=unit*3.44
    print("The Amount Of Electricity Is :",amount)
elif(unit>100 and unit<=300):
    amount=100*3.44 + ((unit - 100 ) * 7.34)
    print("The Amount Of Electricity Is : ",amount)
elif(unit>300 and unit<=500):
    amount=(100*3.44) + (200*7.35) + ((unit-300)*10.36)
    # total = amount
    # total = ( (total - 100) * 5 ) + 100 * 2
    print("The Amount Of Electricity Is : ",amount)
elif(unit>500 and unit<=1000):
    amount=(100*3.44) + (200*7.35) + (300*10.36) + ((unit-600)*11.82)
    print("The Amount Of Electricity Is : ",amount)