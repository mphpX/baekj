n,m=map(int,input().split())
l=list([i for i in range(1,n+1)])
x=m-1
print('<',end='')
while(n!=1):
  print(l[x],end=', ')
  l.pop(x)
  n-=1
  if(n==1):
    break
  x=(x+m-1)%n
print(l[0],'>',sep='')