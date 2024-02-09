import sys
n=int(input())
l=[0]*10001
for i in range(n):
  l[int(sys.stdin.readline())]+=1
for i in range(10001):
  for j in range(l[i]):
    print(i)