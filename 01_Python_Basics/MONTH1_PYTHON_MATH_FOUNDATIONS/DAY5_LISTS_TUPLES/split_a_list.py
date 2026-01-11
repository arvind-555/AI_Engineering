# DAY5 p9 split a list in positive numbers and negative numbers 
def split_in(lst):
    pos_list = []
    neg_list = []
    zero_list = []
    for item in lst:
        if item > 0:
            pos_list.append(item)
        elif item < 0:
            neg_list.append(item)
        else:
            zero_list.append(item)
    return pos_list, neg_list, zero_list
n = int(input("Enter the size of the list: "))
lst = []

for i in range(n):
    num = int(input("Enter element: "))
    lst.append(num)

print("Original list:", lst)

pos , neg , zero = split_in(lst)

print("the splited elements are : ",pos,neg,zero)