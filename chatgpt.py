python = int(input("Enter The Marks Of Python : "))
daa = int(input("Enter The Marks Of DAA : "))
cn = int(input("Enter The Marks Of CN : "))
dwm = int(input("Enter The Marks Of DWM : "))
java = int(input("Enter The Marks Of Java : "))

if python < 0 or python > 100:
    print("Enter Valid Marks")
elif daa < 0 or daa > 100:
    print("Enter Valid Marks")
elif cn < 0 or cn > 100:
    print("Enter Valid Marks")
elif dwm < 0 or dwm > 100:
    print("Enter Valid Marks")
elif java < 0 or java > 100:
    print("Enter Valid Marks")
else:
    percent = (python + daa + cn + dwm + java) / 5

    print("The Percentage Is : ", percent)

    # Grade Calculate

    if percent > 75 and percent <= 100:
        print("Student Is In Distinction")
    elif percent <= 75 and percent > 60:
        print("Student Is In A Grade")
    elif percent <= 60 and percent > 40:
        print("Student Is In B Grade")
    elif percent <= 40 and percent > 20:
        print("Student Is In C Grade")
    else:
        print("Student Is Fail")
