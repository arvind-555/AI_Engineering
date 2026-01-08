## def sum_of_digits(n):
def sum_of_digits(n):
    sumo = 0
    while n>0:
       lastdig = n%10
       sumo = sumo + lastdig
       n = n//10
    return sumo

n = int(input("enter a number : "))
result = sum_of_digits(n)
print("the sum of digits is : ", result)