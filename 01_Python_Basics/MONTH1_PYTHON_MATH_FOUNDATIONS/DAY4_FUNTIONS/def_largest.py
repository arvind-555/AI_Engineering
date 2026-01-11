def largest(a, b, c):
    if a==b==c:
        return "All the numbers are equal"
    elif a==b:
        return " Both A and B are the greatest number"
    elif a==c:
        return " Both A and C are the greatest number"
    elif c==b:
        return "Both C and B are the greatest number"
    else:        
     if a>=b and a>=c:
        return "A ia the greatest number"
     elif b>=a and b>=c:
        return "B is the greatest number"
     else:
        return "C is the greatest number"
a = int(input("enter the value of a : "))
b = int(input("enter the value of b : "))
c = int(input("enter the value of c : "))
result = largest(a,b,c)
print (result)