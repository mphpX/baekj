import sys
n=int(input())

dp=[1,3,7]
for i in range(3,n+1):
    dp.append((dp[i-1]*2+dp[i-2])%9901)
print(dp[n])