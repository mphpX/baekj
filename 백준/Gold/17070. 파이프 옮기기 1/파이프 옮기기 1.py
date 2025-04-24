import sys
sys.setrecursionlimit(10**7)
input=sys.stdin.readline
n=int(input())
graph=[list(map(int,input().split())) for _ in range(n)]
dx=[0,1,1]
dy=[1,1,0]
dp=[[[0 for _ in range(3)] for _ in range(n)] for _ in range(n)]
for i in range(1,n):
    if(graph[0][i]==0):
        dp[0][i][0]=1
    else: break
for i in range(n):
    for j in range(1,n):
        for k in range(3):
            n_x,n_y=i+dx[k],j+dy[k]
            if(0<=n_x<n and 0<=n_y<n and graph[n_x][n_y]==0):
                if(k==0):
                    dp[n_x][n_y][k]=dp[i][j][0]+dp[i][j][1]
                elif(k==1):
                    if(graph[n_x][j]==0 and graph[i][n_y]==0):
                        dp[n_x][n_y][k]=dp[i][j][0]+dp[i][j][1]+dp[i][j][2]
                else:
                    dp[n_x][n_y][k]=dp[i][j][1]+dp[i][j][2]

print(sum(dp[n-1][n-1]))