string = input("Enter The String : ")
print(string)
character = 0
count = 1
for i in string:
    character=character+1
    if(i==" "):
        count=count+1
print("The Number Of Words Are : ",count)
print("The Number Of Characters Are : ",character)
