#day 2 p4 || leap year 
n = int(input("Enter a year : "))
if n%400 == 0 or n%4==0 and n%100 != 0:
    print(f"{n}  is a leap year")
else:
    print(f"{n} is Not a leap year")