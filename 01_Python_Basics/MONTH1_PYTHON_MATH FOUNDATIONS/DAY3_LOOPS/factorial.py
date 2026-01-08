# DAY 3 P6 - count nuumber of digits
n = int(input("enter a number : "))
count = 0
while n>0:
    count = count+1
    n = n//10
print("the number of digits is : ",count)