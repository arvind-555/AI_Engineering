# DAY 5 - P1 creationg a list with user input
print(">>> RUNNING CREATE_LIST.py DAY 5 <<<")
n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    num = int(input("Enter number: "))
    lst.append(num)

print(lst)
