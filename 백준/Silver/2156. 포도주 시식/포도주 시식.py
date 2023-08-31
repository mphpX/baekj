import sys
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
dp=[]
for i in range(n):
    if(i==0):dp.append(arr[0])
    elif(i==1):dp.append(arr[0]+arr[1])
    elif(i==2):dp.append(max(arr[0]+arr[2],arr[1]+arr[2]))
    else:
        m=0
        for j in range(i-2):
            if(m<dp[j]):m=dp[j]
        dp.append(max(dp[i-2],m+arr[i-1])+arr[i])
print(max(dp))