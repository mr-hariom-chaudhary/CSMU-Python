cost = int(input("Enter The Cost Of Bike : "))

if(cost > 100000):
    tax=cost*15/100
    total=cost+tax
elif(cost >= 50000 and cost <= 100000):
    tax=cost*10/100
    total=cost+tax
elif(cost < 50000):
    tax=cost*5/100
    total=cost+tax
print("The Tax Of Bike Is : ",tax)
print("The Total Cost Of Bike Is : ",total)