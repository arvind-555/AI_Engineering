#DAY2 p8 electricity bill
n = int(input("enter the units of electricity consumed"))
a = n*1
if n <= 100:
  print("the total amount to be paid is :",a)
elif n > 100 and n<=200:
    b = 2 * (n-100) + 100
    print("the total amount to be paid is :",b)
else:
   c = n-200
   d = (3*c) + (2*100) + 100
   print("the total amount to be paid is :",d)