# DAY 5 P8 - sort a list (basic)

def sort_list(lst):
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            if lst[i] > lst[j]:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
    return lst

n = int(input("Enter the size of the list: "))
lst = []

for i in range(n):
    num = int(input("Enter element: "))
    lst.append(num)

print("Original list:", lst)

sorted_list = sort_list(lst)
print("Sorted list:", sorted_list)
