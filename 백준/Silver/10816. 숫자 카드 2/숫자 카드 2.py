import sys
n=int(input())
d=dict()
a=list(map(int,sys.stdin.readline().split()))
m=int(input())
b=list(map(int,sys.stdin.readline().split()))
for i in a:
  if i in d:
    d[i]+=1
  else:
    d[i]=1
for i in b:
  if i in d:
    print(d[i],end=' ')
  else:
    print(0,end=' ')