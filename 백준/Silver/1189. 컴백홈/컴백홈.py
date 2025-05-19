from collections import deque
import sys
input= sys.stdin.readline
r,c,k=map(int,input().split())
graph=[input().strip() for _ in range(r)]
visited=[[False for _ in range(c)] for _ in range(r)]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
ans=0
def dfs(x,y,ct):
    if(x==0 and y==c-1):
        if(ct==k):
            global ans
            ans+=1
        return
    for i in range(4):
        n_x=x+dx[i]
        n_y=y+dy[i]
        if(0<=n_x<r and 0<=n_y<c):
            if(visited[n_x][n_y]==False and graph[n_x][n_y]=='.'):
                visited[n_x][n_y]=True
                dfs(n_x,n_y,ct+1)
                visited[n_x][n_y]=False
visited[r-1][0]=True
dfs(r-1,0,1)
print(ans)