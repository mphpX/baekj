import sys
n=int(input())
arr=list(map(int,input().split()))
dp=[1]
for i in range(1,n):
    m=0
    for j in range(i):
        if(arr[i]<arr[j] and m<dp[j]):
            m=dp[j]
    dp.append(m+1)
print(max(dp))