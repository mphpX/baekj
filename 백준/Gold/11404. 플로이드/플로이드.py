import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
m=int(input())
graph=[[] for _ in range(n+1)]
dp=[[float('inf') for _ in range(n+1)]for _ in range(n+1)]
for i in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((c,b))
for i in range(1,n+1):
    dp[i][i]=0
    for weight, next in graph[i]:
        dp[i][next]= min(weight,dp[i][next])
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(dp[i][j]>dp[i][k]+dp[k][j]):
                dp[i][j]=dp[i][k]+dp[k][j]
for i in range(1,n+1):
    for j in range(1,n+1):
        if(dp[i][j]==float('inf')):
            print(0,end=' ')
        else: print(dp[i][j],end=' ')
    print()