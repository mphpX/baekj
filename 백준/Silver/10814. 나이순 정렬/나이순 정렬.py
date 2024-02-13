import sys
n=int(input())
l=[]
for i in range(n):
  a=list(map(str,sys.stdin.readline().split()))
  a[0]=int(a[0])
  l.append(a)

l.sort(key= lambda x: x[0])
for i in l:
  print(i[0],i[1])