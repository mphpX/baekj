from collections import deque
import sys
n=int(input())
l=deque(enumerate(map(int,sys.stdin.readline().split())))
while(n!=0):
  idx,paper = l.popleft()
  n-=1
  print(idx+1,end=' ')
  if(n==0): 
    break
  if(paper>0):
    l.rotate(-paper+1)
  else:
    l.rotate(-paper)