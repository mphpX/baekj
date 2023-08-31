import sys
n=int(input())
arr=list(map(int,input().split()))
m=0
dp=[arr[0]]
for i in range(1,n):
    dp.append(max(dp[i-1]+arr[i],arr[i]))
print(max(dp))