from collections import deque
import sys
n=int(input())
l=deque([])
for i in range(n):
  m=list(map(int,sys.stdin.readline().split()))
  if(m[0]==1):
    l.appendleft(m[1])
  elif(m[0]==2):
    l.append(m[1])
  elif(m[0]<=4 or 7<=m[0]):
    if(len(l)==0):
      print(-1)
    else:
      if(m[0]<=4):
        if(m[0]==4):
          print(l[-1])
          l.pop()
        else:
          print(l[0])
          l.popleft()
      elif(m[0]==7):
        print(l[0])
      else:
        print(l[-1])
  elif(m[0]==5):
    print(len(l))
  else:
    if(len(l)==0):
      print(1)
    else:
      print(0)