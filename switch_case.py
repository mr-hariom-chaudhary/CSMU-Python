num1 = int(input("Enter The First Number : "));
num2 = int(input("Enter The Second Number : "));
sign = int(input("Enter The Operator : "));

add = num1+num2;
sub = num1-num2;
mul = num1*num2;
div = num1/num2;

switch(sign)
    case sign == "+" :
        print("The Addition Is : ",add);
        break;
case '-' :
print("The Substraction Is : ",sub);
break;
case '*' :
print("The Multiplication Is : ",mul);
break;
case '/' :
print("The Division Is : ",div);
break;