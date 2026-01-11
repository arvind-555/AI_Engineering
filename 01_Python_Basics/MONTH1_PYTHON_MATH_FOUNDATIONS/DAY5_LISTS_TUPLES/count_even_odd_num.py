# DAY 5 P4 count even and odd numberss in a list
def count_even_odd_number(lst1):
    even = 0
    odd = 0
    for num in lst1:
        if num%2==0:
            even = even + 1 
        else:
            odd = odd + 1
    return even , odd 
n = int(input("enter the size of the list : "))
lst1 = []
for i in range(n):
    num = int(input("Enter the number : "))
    lst1.append(num)
print("the entered nummbers are : ",lst1)  
even_count, odd_count  = count_even_odd_number(lst1)
print("the number of even number in the list is : ", even_count)
print("the nummber of odd number in the result is : ",odd_count) 