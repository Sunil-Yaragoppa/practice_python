a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
number = int (input ("Enter a number : "))
b=[x for x in a if x < number]
for x in b :
  print(x)
