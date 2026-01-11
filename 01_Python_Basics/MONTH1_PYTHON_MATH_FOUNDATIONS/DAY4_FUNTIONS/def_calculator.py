# DAY 4 p7 calculator
def calculator(a,b,n):
    if n>4 or n<1:
      return "BRO CHOOSE THE NUMBERS BETWEEN 1-4"
    else:   
     if n == 1:
      c = a+b
      return c
     elif  n==2:
       c = a-b
       return c
     elif n==3:
       c = a*b
       return c
     else:
      if b==0:
       return "INDiVISIBLE"
      else:
       c = a/b
       return c
print(" 1 for ADDITION ")
print(" 2 for SUBTRACTION ")
print(" 3 for MULTIPLICATION")
print(" 4 for DIVISION")
n = int(input("Enter your choice :"))
a = int(input("enter the value of a : "))
b = int(input("enter the value of b : "))
result = calculator(a,b,n)
print (result)