import sys
input=sys.stdin.readline
n=int(input())
child=[int(input()) for _ in range(n)]
dp=[1 for _ in range(n)]
post=0
for i in range(1,n):
    for j in range(i):
        if(child[i]>child[j]):
            dp[i]=max(dp[i],dp[j]+1)
print(n-max(dp))