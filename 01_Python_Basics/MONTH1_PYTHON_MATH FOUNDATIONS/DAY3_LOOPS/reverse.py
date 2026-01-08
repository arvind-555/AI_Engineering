# DAY 3 p7 - reverse
n = int(input("enter a number : "))
reverse = 0
while n>0:
 lastdig = n%10
 reverse = reverse*10 + lastdig
 n = n//10
print ("the reverse is :",reverse)