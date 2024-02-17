import sys
n,m=map(int,input().split())
o=[]
ct=0
for i in range(n):
  a=sys.stdin.readline().strip()
  o.append(a)
for i in range(m):
  a=sys.stdin.readline().strip()
  if a in o:
    ct+=1
print(ct)