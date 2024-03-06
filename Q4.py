# write a pyhton program to check enetered string is palindrome or not

string = input("Enter The String : ")
rev = ""
for i in string:
    rev = i + rev
if(string==rev):
    print(string," It Is Palindrome")
else:
    print(string," It Is Not A Palindrome")