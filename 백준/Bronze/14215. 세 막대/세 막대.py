x=list(map(int,input().split()))
if(max(x)<sum(x)-max(x)):
  print(sum(x))
else:
  print(sum(x)-max(x)-1+sum(x)-max(x))