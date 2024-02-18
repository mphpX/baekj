import sys
n,m=map(int,input().split())
d=dict()
l=[]
for i in range(n):
  a=sys.stdin.readline().strip()
  d[a]=1
for i in range(m):
  a=sys.stdin.readline().strip()
  if a in d:
    l.append(a)
l.sort()
print(len(l))
for i in l:
  print(i)
