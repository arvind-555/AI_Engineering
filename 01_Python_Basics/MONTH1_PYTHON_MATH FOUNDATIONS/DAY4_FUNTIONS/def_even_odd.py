def even_odd(n):
    if n % 2 == 0:
      return "it is an even number"
    else :
     return"it is an odd numbr !"
n = int(input("enter a number"))
c = even_odd(n)
print(c)