n=int(input())
l=[0]*2001
for i in range(n):
  b=int(input())
  l[b+1000]+=1
for i in range(2001):
  if(l[i]>0):
    print(i-1000)
