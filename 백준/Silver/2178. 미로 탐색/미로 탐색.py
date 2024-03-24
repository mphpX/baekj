import sys
from collections import deque
dx=[0,0,1,-1]
dy=[1,-1,0,0]
n,m=map(int,sys.stdin.readline().split())
l=[]
for i in range(n):
    a=list(map(int,sys.stdin.readline().strip()))
    l.append(a)
def bfs(x,y):
    q=deque()
    q.append((x,y))
    while(q):
        c,d=q.popleft()
        for i in range(4):
            nx=c+dx[i]
            ny=d+dy[i]
            if(0<=nx<n and 0<=ny<m):
                if l[nx][ny]==1:
                    q.append((nx,ny))
                    l[nx][ny]=l[c][d]+1
bfs(0,0)
print(l[n-1][m-1])