n=int(input())
result=0
x=0
for i in range(1,n):
  x=i
  result=x
  while(x):
    result+=x%10
    x//=10
  if(result==n):
    x=-1
    result=i
    break
if(x==-1):
  print(result)
else:
  print("0")