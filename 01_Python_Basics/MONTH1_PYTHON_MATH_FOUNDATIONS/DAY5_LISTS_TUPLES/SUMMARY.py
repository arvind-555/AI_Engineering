# DAY5 P10 summarise a list 
def sum_of_list(lst):
    result = 0
    for num in lst:
        result = result + num
    return result

def find_max(lst):
    current_max = lst[0]
    for num in lst:
        if num > current_max:
            current_max = num
    return current_max

def find_min(lst):
    current_min = lst[0]
    for num in lst:
        if num < current_min:
            current_min = num
    return current_min

n = int(input("Enter the size of the list: "))
lst = []

for i in range(n):
    num = int(input("Enter element: "))
    lst.append(num)
print("Original list:", lst)
length = len(lst)
print ("the total number of elementss in the list are : ",length)

summ = sum_of_list(lst)
print ("The sum of the list is :",summ)

maxx = find_max(lst)
print("The largest number in the list is : ",maxx)

minn = find_min(lst)
print("the smallest element in the list is : ",minn)