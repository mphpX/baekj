import sys
from collections import deque
t=int(sys.stdin.readline())
for i in range(t):
    n,m=map(int,sys.stdin.readline().split())
    l=deque(map(int,sys.stdin.readline().split()))
    ct=0
    while(True):
        if(max(l)>l[0]):
            x=l.popleft()
            l.append(x)
            if(m==0):
                m=len(l)-1
            else:
                m-=1
        else:
            ct+=1
            if(m==0):
                break
            else:
                l.popleft()
                m-=1
    print(ct)