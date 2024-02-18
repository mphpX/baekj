import sys
n=int(input())
m=[]
o=dict()
ct=0
for i in range(n):
  a,b=map(str,sys.stdin.readline().split())
  o[a]=b
for i,j in o.items():
  if(j=='enter'):
    m.append(i)
m.sort(reverse=True)
for i in m:
  print(i)