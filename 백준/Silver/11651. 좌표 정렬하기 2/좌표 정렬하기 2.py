import sys
n=int(input())
l=[]
for i in range(n):
  a=list(map(int,sys.stdin.readline().split()))
  l.append(a)
l.sort(key = lambda x: (x[1],x[0]))

for i in range(n):
  print(l[i][0],l[i][1])