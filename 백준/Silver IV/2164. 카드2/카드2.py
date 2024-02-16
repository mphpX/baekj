import sys
from collections import deque
n=int(input())
l=[]
l=deque(l)
for i in range(1,n+1):
  l.append(i)
while(len(l)!=1):
  l.popleft()
  a=l[0]
  l.popleft()
  l.append(a)
print(l[0])