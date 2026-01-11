# DAY 5 - P2 - take input from user, store them in a list and find the sum

def sum_of_list(lst):
    result = 0
    for num in lst:
        result = result + num
    return result

n = int(input("ENTER list size: "))
lst = []

for i in range(n):
    num = int(input("Enter the number that you want to store in the list: "))
    lst.append(num)

summ = sum_of_list(lst)
print("The sum of the numbers in the list is:", summ)
