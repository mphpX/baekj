import sys
from collections import deque
n,m=map(int,sys.stdin.readline().split())
l=[0 for i in range(100001)]
def bfs(x):
    q=deque()
    q.append(x)
    while(q):
        c=q.popleft()
        if(c==m):
            print(l[m])
            break
        for nx in (c-1,c+1,c*2):
            if(0<=nx<=100000 and l[nx]==0):
                l[nx]=l[c]+1
                q.append(nx)  
bfs(n)