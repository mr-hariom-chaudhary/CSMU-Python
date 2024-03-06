# write a python program to reverse a string

string = input("Enter The String You Want To Reverse : ")
reversed_string = ""
for char in string:
    reversed_string = char + reversed_string
print("Original String : ", string)
print("Reversed String : ", reversed_string)