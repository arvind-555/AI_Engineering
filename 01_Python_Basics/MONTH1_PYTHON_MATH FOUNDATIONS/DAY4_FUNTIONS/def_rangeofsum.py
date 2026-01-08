#day 4 p8 - range of sum
def sum_upto_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
n = int(input("enter a number :" ))
result = sum_upto_n(n)
print(result)