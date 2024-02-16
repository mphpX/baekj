import sys
from collections import deque
n=int(input())
l=[]
l=deque(l)
for i in range(n):
  m=list(map(str,sys.stdin.readline().split()))
  if(m[0]=='push'):
    l.append(int(m[1]))
  elif(m[0]=='pop'):
    if(len(l)!=0):
      print(l[0])
      l.popleft()
    else:
      print(-1)
  elif(m[0]=='size'):
    print(len(l))
  elif(m[0]=='empty'):
    if(len(l)==0):
      print(1)
    else:
      print(0)
  elif(m[0]=='front'):
    if(len(l)!=0):
      print(l[0])
    else:
      print(-1)
  elif(m[0]=='back'):
    if(len(l)!=0):
      print(l[-1])
    else:
      print(-1)