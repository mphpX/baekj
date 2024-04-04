import sys
from collections import deque
n,m=map(int,sys.stdin.readline().split())
visited=[[0 for _ in range(m)] for _ in range(n)]
l=[]
p=0
q=0
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for i in range(n):
    a=list(map(int,sys.stdin.readline().split()))
    l.append(a)
for i in range(n):
    for j in range(m):
        if(l[i][j]==2):
            p=i
            q=j
            l[i][j]=0
            break
def bfs(x,y):
    d=deque()
    d.append((x,y))
    visited[x][y]=1
    while d:
        x1,y1=d.popleft()
        for i in range(4):
            nx,ny=x1+dx[i],y1+dy[i]
            if(0<=nx<n and 0<=ny<m and l[nx][ny]==1 and visited[nx][ny]==0):
                l[nx][ny]=l[x1][y1]+1
                d.append((nx,ny))
                visited[nx][ny]=1
bfs(p,q)
for i in range(n):
    for j in range(m):
        if(visited[i][j]==0 and l[i][j]==1):
            print(-1,end=' ')
        else:
            print(l[i][j], end= ' ')
    print()