import sys
n=int(input())
arr=list(map(int,input().split()))
dp=[1]
for i in range(1,n):
    m=1
    for j in range(i):
       if(arr[i]>arr[j] and dp[j]+1>m):
           m=dp[j]+1
    dp.append(m)
print(max(dp))