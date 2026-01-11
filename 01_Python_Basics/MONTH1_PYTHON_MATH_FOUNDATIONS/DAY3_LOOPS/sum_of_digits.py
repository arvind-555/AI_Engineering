# day 4 p10 - sum of digits
n = int(input("enter a number : "))
sumo = 0
while n>0:
    lastdig = n%10
    sumo = sumo + lastdig
    n = n//10
print (sumo)