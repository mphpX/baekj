import sys
n,m=map(int,input().split())
d=dict()
for i in range(n):
  a=sys.stdin.readline().strip()
  d[a]=i+1
  d[str(i+1)]=a
for j in range(m):
  a=sys.stdin.readline().strip()
  if(a.isalpha()==True):
    print(d[a])
  else:
    print(d[a])