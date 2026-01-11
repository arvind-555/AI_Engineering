# DAY 5 P7 - remove duplicates from a list

def remove_duplicate(lst):
    new_list = []
    for element in lst:
        if element not in new_list:
            new_list.append(element)
    return new_list

n = int(input("Enter the size of the list: "))
lst = []

for i in range(n):
    num = int(input("Enter the elements that you want to store in the list: "))
    lst.append(num)

print("The numbers you entered are:", lst)

lst2 = remove_duplicate(lst)
print("The new list without duplicate elements:", lst2)
