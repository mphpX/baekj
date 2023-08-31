import sys
n=int(input())
dp=[0,[0,1]]
for i in range(2,n+1):
    num=[dp[i-1][0]+dp[i-1][1],dp[i-1][0]]
    dp.append(num)
print(dp[n][0]+dp[n][1])