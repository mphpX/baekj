import sys
n=int(input())
x=[]
for i in range(n):
  a=list(map(int,sys.stdin.readline().split()))
  x.append(a)
x.sort()
for i in range(n):
  print(x[i][0],x[i][1])