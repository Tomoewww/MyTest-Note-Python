num = int(input())
for x in range(1, num+1):
  for y in range(x,num):
    print (" ",end="")
  for y in range(x * 2 - 1):
    print("*",end="")
  for y in range(1,5 - x):
    print(" ",end="")
  print()
for x in range(num-1, 0 , -1):
  for y in range(num, x):
    print (" ",end="")
  for y in range(1,x + 1):
    print("*",end="")
  for y in range(2,x + 1):
    print(" ",end="")  
  print()