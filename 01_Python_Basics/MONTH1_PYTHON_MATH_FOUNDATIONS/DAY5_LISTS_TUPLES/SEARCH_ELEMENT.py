# DAY 5 P6 SEARCH AN ELEMENT In a list
def find_position(lst, element): # we are using two parameters because the function needs two inputs: the list to search (lst) and the value to search for (element).
    for i in range(len(lst)): # element is taken as a parameter (not key) so the function remains independent and reusable; key is only the variable name used outside the function to pass the value.
        if lst[i] == element:
            return i+1
    return -1

n = int(input("Enter the size of the list: "))
lst = []

for i in range(n):
    num = int(input("Enter element: "))
    lst.append(num)

key = int(input("Enter element to find: "))

pos = find_position(lst, key)

if pos != -1:
    print("Element found at position:", pos)
else:
    print("Element not found in the list")
