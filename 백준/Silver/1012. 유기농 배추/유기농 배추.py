import sys
from collections import deque
sys.setrecursionlimit(10**9)
visited=[]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
def dfs(graph,x,y,n,m):
    visited[x][y]=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if(0<=nx<n and 0<=ny<m):
            if(visited[nx][ny]==0 and graph[nx][ny]==1):
                dfs(graph,nx,ny,n,m)
t=int(sys.stdin.readline())
for i in range(t):
    m,n,k=map(int,sys.stdin.readline().split())
    visited=[[0 for i in range(m)] for i in range(n)]
    l=[[0 for i in range(m)]for i in range(n)]
    result=0
    for i in range(k):
        a,b=map(int,sys.stdin.readline().split())
        l[b][a]=1
    for i in range(n):
        for j in range(m):
            if(visited[i][j]==0 and l[i][j]==1):
                dfs(l,i,j,n,m)
                result+=1
    print(result)