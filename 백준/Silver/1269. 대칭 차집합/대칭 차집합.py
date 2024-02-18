import sys
n,m=map(int,input().split())
d=dict()
a=map(int,sys.stdin.readline().split())
for i in a:
  d[i]=1
b=map(int,sys.stdin.readline().split())
ct=0
for i in b:
  if i in d:
    d[i]-=1
  else:
    d[i]=1
for i in d:
  if(d[i]!=0):
    ct+=1
print(ct)