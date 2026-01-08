#DAY 2 p6 voting eligibility
n = int(input("Enter your Age"))
if n <= 0:
 print("INVALID AGE")
else:
    if n<18:
        print("YOU ARE UNDER AGE")
    else:
        print("YOu are eligible")