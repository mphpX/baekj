money=[25,10,5,1]
x=int(input())
for i in range(x):
  y=int(input())
  for j in range(4):
    print(y//money[j],end=' ')
    y-=y//money[j]*money[j]
  print()