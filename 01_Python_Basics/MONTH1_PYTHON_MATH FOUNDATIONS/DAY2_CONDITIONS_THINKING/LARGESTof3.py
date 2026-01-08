#DAY-2 p3
n = int(input("enter you result  : "))
if n>100 or n<0:
    print("INVALID number")
else:
    if n<40:
      print("you are fail !")
    elif n>=40 and n<=59 :
      print("JUST pass")
    elif n >= 60 and n<=74:
      print("First class")
    else:
      print("Distinction")