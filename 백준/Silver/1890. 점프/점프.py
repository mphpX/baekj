import sys
input=sys.stdin.readline
n= int(input())
graph=[list(map(int,input().split())) for _ in range(n)]
dx=[1,0]
dy=[0,1]
dp=[[0 for _ in range(n)] for _ in range(n)]
dp[0][0]=1
for i in range(n):
    for j in range(n):
        if(graph[i][j]==0):
            break
        for k in range(2):
            nx,ny=i+dx[k]*graph[i][j],j+dy[k]*graph[i][j]
            if(0<=nx<n and 0<=ny<n):
                if(dp[i][j]>0):
                    dp[nx][ny]+=dp[i][j]
print(dp[n-1][n-1])