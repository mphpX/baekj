import sys
from collections import deque
n,m=map(int,sys.stdin.readline().split())
visited=[[0 for _ in range(m) ]for _ in range(n)]
l=[]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
d=0
p=0
q=0
ct=0
for i in range(n):
    a=sys.stdin.readline().strip()
    for j in range(m):
        if(a[j]=='I'):
            p=i
            q=j
    l.append(a)
def bfs(x,y):
    d=deque()
    d.append((x,y))
    visited[x][y]=1
    while(d):
        e,f=d.popleft()
        for i in range(4):
            nx=e+dx[i]
            ny=f+dy[i]
            if(0<=nx<n and 0<=ny<m and (l[nx][ny]=='O' or l[nx][ny]=='P') and visited[nx][ny]==0):
                if(l[nx][ny]=='P'):
                    global ct
                    ct+=1
                visited[nx][ny]=1
                d.append((nx,ny))

bfs(p,q)
if(ct==0):
    print('TT')
else:
    print(ct)