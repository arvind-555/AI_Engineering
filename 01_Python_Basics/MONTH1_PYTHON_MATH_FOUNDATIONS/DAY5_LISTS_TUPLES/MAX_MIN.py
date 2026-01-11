# DAY 5 P3 find the max and min in a list
def find_max(lst):
    current_max = lst[0]
    for num in lst:
        if num > current_max:
            current_max = num
        else:
            current_max = lst[0]
    return current_max

def find_min(lst):
    current_min = lst[0]
    for num in lst:
        if num < current_min:
            current_min = num
        else:
            current_min = lst[0]
    return current_min
        

n = int(input("Enter the size of the list : "))
lst = []
for i in range(n):
    num = int(input("enter the number you want to store in the list : "))
    lst.append(num)
print("The entered numbers in the list are : ",lst)
max = find_max(lst)
min = (find_min(lst))
print("the largest number in the list is : ", max)
print("the smallest number in the list is : ",min)

