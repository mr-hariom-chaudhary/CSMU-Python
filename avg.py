num = int(input("Enter The Number You Want To Find Average Of : "))
sum=0
for i in range(num):
    numbers = int(input("Enter The Number : "))
    sum=sum+numbers
avg=sum/num    
print(avg)