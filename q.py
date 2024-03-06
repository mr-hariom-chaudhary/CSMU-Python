# write a program to find sum of all the odd number from 1-50

n = 50
sum = 0
for x in range(1,n+1):
    if(x%2!=0):
        sum = sum + x
print(sum)