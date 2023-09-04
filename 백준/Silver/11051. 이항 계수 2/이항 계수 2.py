import sys
n,k=map(int,input().split())
dp=[1,1]
for i in range(2,n+1):
    dp.append((dp[i-1]*i))
print((dp[n]//(dp[k]*dp[n-k]))%10007)