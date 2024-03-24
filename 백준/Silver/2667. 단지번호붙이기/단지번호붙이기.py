import sys
from collections import deque
sys.setrecursionlimit(10**9)
n=int(sys.stdin.readline())
l=[]
result=[]
for i in range(n):
    a=list(sys.stdin.readline().strip())
    l.append(a)
visited=[[0 for i in range(n)] for i in range(n)]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
ct=0
def dfs(graph,x,y):
    visited[x][y]=1
    global ct
    ct+=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if(0<=nx<n and 0<=ny<n):
            if(visited[nx][ny]==0 and graph[nx][ny]=='1'):
                dfs(graph,nx,ny)
for i in range(n):
    for j in range(n):
        ct=0
        if(visited[i][j]==0 and l[i][j]=='1'):
            dfs(l,i,j)
            result.append(ct)
result.sort()
print(len(result))
for i in result:
    print(i)