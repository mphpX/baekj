import sys
n=int(input())
arr=list(map(int,input().split()))
dp=[arr[0]]
for i in range(1,n):
    m=0
    for j in range(i):
        if(arr[i]>arr[j] and m<dp[j]):
            m=dp[j]
    dp.append(m+arr[i])
print(max(dp))