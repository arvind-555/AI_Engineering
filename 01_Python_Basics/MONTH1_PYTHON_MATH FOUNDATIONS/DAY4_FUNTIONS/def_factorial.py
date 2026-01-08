def fact(n):
    c = 1
    for n in range (1,n+1):
        c *= n
    return c

n = int(input("enter a number : "))
result = fact(n)
print(result)