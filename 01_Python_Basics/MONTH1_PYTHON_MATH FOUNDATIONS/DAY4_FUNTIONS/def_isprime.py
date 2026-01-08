# is prime DAY 4 - p6
def is_prime(n):
    count = 0 
    for i in range(1,n):
        if n%i==0:
            count=count+1
    if count>2:
        return "It is not a prime number"
    else:
        return "It is a prime number"

n = int(input("Enter a number : "))
result = is_prime(n)
print(result)