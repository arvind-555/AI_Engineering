##### day 2 p5 || calculator
print(" 1 for ADDITION ")
print(" 2 for SUBTRACTION ")
print(" 3 for MULTIPLICATION")
print(" 4 for DIVISION")
n = int(input("Enter your choice :"))
if n>4 or n<1:
    print("BRO CHOOSE THE NUMBERS BETWEEN 1-4")
else:   
  a = int(input("ennter the value of a : "))
  b = int(input("enter the value of b : "))
  if n == 1:
   c = a+b
   print(f"the addition of {a} and {b} is : ",c)
  elif  n==2:
   c = a-b
   print(f"the subtraction of {a} and {b} is : ",c)
  elif n==3:
   c = a*b
   print(f"the multiplication of {a} and {b} is : ",c) 
  else:
     if b==0:
      print("INDiVISIBLE")
     else:
      c = a/b
      print(f"the division of {a} and {b} is : ",c)