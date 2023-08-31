import sys
arr=[]
n=int(input())
for i in range(n):
    num=list(map(int,sys.stdin.readline().split()))
    arr.append(num)
dp=[[arr[0][0],arr[0][1],arr[0][2]]]
for i in range(1,n):
    num=[]
    for j in range(3):
        if(j==0):
            num.append(min(dp[i-1][1],dp[i-1][2])+arr[i][j])
        elif(j==1):
            num.append(min(dp[i-1][0],dp[i-1][2])+arr[i][j])
        else:
            num.append(min(dp[i-1][1],dp[i-1][0])+arr[i][j])
    dp.append(num)
print(min(dp[n-1]))
