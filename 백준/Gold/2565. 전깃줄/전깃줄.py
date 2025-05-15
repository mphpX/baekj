import sys
input=sys.stdin.readline
n=int(input())
graph=[list(map(int,input().split())) for _ in range(n)]
dp=[1 for _ in range(n)]
graph.sort()
for i in range(1,n):
    for j in range(i):
        if(graph[j][1]<graph[i][1]):
            dp[i]=max(dp[j]+1,dp[i])

print(n-max(dp))