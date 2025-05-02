import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[[0 for _ in range(m)]for _ in range(n)]
visited=[[False for _ in range(m)]for _ in range(n)]
q=list(map(int,input().split()))
for i in range(q[0]):
    graph[q[i*2+1]-1][q[i*2+2]-1]=1
k=list(map(int,input().split()))
for i in range(k[0]):
    graph[k[i*2+1]-1][k[i*2+2]-1]=2
p=list(map(int,input().split()))
for i in range(p[0]):
    graph[p[i*2+1]-1][p[i*2+2]-1]=-1
    visited[p[i*2+1]-1][p[i*2+2]-1]=True
def kbfs(x,y):
    q=deque([(x,y)])
    dx=[1,2,1,2,-1,-2,-1,-2]
    dy=[2,1,-2,-1,2,1,-2,-1]
    visited[x][y]=True
    for i in range(8):
        next_x, next_y=x+dx[i],y+dy[i]
        if(0<=next_x<n and 0<=next_y<m):
            if(graph[next_x][next_y]==0):
                visited[next_x][next_y]=True
def qbfs(x,y):
    dx=[1,0,-1,0,1,-1,1,-1]
    dy=[0,1,0,-1,1,-1,-1,1]
    visited[x][y]=True
    for i in range(8):
        next_x, next_y=x+dx[i],y+dy[i]
        while(0<=next_x<n and 0<=next_y<m):
            if(graph[next_x][next_y]!=0):
                break
            else:
                visited[next_x][next_y]=True
            next_x, next_y=next_x+dx[i],next_y+dy[i]
for i in range(q[0]):
    qbfs(q[i*2+1]-1,q[i*2+2]-1)
for i in range(k[0]):
    kbfs(k[i*2+1]-1,k[i*2+2]-1)
ans=0
for i in range(n):
    for j in range(m):
        if(visited[i][j]==False):
            ans+=1
print(ans)