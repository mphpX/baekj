import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]
dx=[0,1,-1,0]
dy=[1,0,0,-1]
ct=0
visited=[[False for _ in range(m)]for _ in range(n)]
cur=0
def bfs(s_x,s_y):
    q=deque([(s_x,s_y)])
    visited[s_x][s_y]=True
    ct=1
    while(q):
        cur_x,cur_y=q.popleft()
        for i in range(4):
            n_x,n_y=cur_x+dx[i],cur_y+dy[i]
            if(0<=n_x<n and 0<=n_y<m):
                if(graph[n_x][n_y]==1 and visited[n_x][n_y]==False):
                    q.append((n_x,n_y))
                    visited[n_x][n_y]=True
                    ct+=1
    return ct
ans=[0]
for i in range(n):
    for j in range(m):
        if(graph[i][j]==1 and visited[i][j]==False):
            ans.append(bfs(i,j))
print(len(ans)-1)
print(max(ans))