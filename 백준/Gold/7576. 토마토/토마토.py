import sys
from collections import deque
n,m=map(int,sys.stdin.readline().split())
l=[]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
result=0
d=deque()
for i in range(m):
    a=list(map(int,sys.stdin.readline().split()))
    l.append(a)
    for j in range(n):
        if(a[j]==1):
            d.append((i,j))
def bfs():
    while(d):
        e,f=d.popleft()
        for i in range(4):
            nx=e+dx[i]
            ny=f+dy[i]
            if(0<=nx<m and 0<=ny<n and (l[nx][ny]==0)):
                l[nx][ny]=l[e][f]+1
                d.append((nx,ny))
bfs()
for i in l:
    for j in i:
        if(j==0):
            print(-1)
            exit(0)
    result=max(result,max(i))
print(result-1)