import sys
from collections import deque
t=int(sys.stdin.readline())
dx=[-2,-2,-1,-1,1,1,2,2]
dy=[-1,1,-2,2,-2,2,-1,1]

def bfs(l,v,x,y,mx,my):
    q=deque()
    q.append((x,y))
    while(q):
        c,d=q.popleft()
        if(c==mx and d==my):
            print(l[mx][my])
            break
        for i in range(8):
            nx=c+dx[i]
            ny=d+dy[i]
            if(0<=nx<v and 0<=ny<v and l[nx][ny]==0):
                l[nx][ny]=l[c][d]+1
                q.append((nx,ny))  

for i in range(t):
    p=int(sys.stdin.readline())
    graph=[[0 for _ in range(p)] for _ in range(p)]
    x1,y1=map(int,sys.stdin.readline().split())
    x2,y2=map(int,sys.stdin.readline().split())
    bfs(graph,p,x1,y1,x2,y2)