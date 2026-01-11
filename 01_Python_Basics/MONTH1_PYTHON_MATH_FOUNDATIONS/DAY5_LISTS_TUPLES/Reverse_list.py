def reverse_list(lst):
    rev_lst = []
    for i in range(len(lst) - 1, -1, -1):
        rev_lst.append(lst[i])
    return rev_lst

n = int(input("Enter the size of the list: "))
lst = []

for i in range(n):
    num = int(input("Enter the elements that you want to store in the list: "))
    lst.append(num)

print("The numbers you entered are:", lst)

reversed_list = reverse_list(lst)
print("The reversed elements are:", reversed_list)
