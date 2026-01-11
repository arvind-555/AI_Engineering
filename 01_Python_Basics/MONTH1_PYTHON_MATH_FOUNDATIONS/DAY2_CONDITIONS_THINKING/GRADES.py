#DAY-2 p10 grades
n = int(input("enter you result  : "))
if n>=100 or n<0:
    print("INVALID number")
else:
    if n>=90 :
      print("A !")
    elif n>=75 and n<=89 :
      print("B")
    elif n >= 60 and n<=74:
      print("C")
    elif n <= 59 and n >= 40:
        print("D")
    else:
      print("F")