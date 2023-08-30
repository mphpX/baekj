import sys
arr=[0]
n=int(input())
for i in range(n):
    arr.append(int(input()))
dp=[0,arr[1]]
for i in range(2,n+1):
    if(i==2):dp.append(arr[1]+arr[2])
    elif(i==3):dp.append(max(arr[1]+arr[3],arr[2]+arr[3]))
    else:dp.append(max(dp[i-2]+arr[i],dp[i-3]+arr[i-1]+arr[i]))
print(dp[n])