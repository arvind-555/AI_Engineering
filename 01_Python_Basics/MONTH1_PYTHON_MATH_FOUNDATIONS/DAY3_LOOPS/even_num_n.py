# DAY 3 p9 - even numbers till n
n = int(input("enter a number  : "))
for i  in range (1,n+1):
  if i % 2==0:
      print(i)
  else:
      continue