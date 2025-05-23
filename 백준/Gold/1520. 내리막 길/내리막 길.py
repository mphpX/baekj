import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000000)
n,m=map(int,input().split())
graph=[ list(map(int,input().split())) for _ in range(n)]
dp=[[-1 for _ in range(m)]for _ in range(n)]
dx=[1,0,-1,0]
dy=[0,1,0,-1]

def dfs(x,y):
    if(x==n-1 and y==m-1):
        return 1
    if(dp[x][y]!=-1):
        return dp[x][y]
    dp[x][y]=0
    for i in range(4):
        n_x,n_y=x+dx[i], y+dy[i]
        if(0<=n_x<n and 0<=n_y<m):
            if(graph[n_x][n_y]<graph[x][y]):
                dp[x][y]+= dfs(n_x,n_y)
    return dp[x][y]
dfs(0,0)
print(dp[0][0])