#DAY 2 p9 to check triangle or not
a = int(input("enter the length of side 'a' : "))
b = int(input("enter the length of side 'b' : "))
c = int(input("enter the length of side 'c' : "))
if a+b > c and a+c > b and b+c > a:
    print("they can form a triangle")
else:
    print("they cannot for a triangle")