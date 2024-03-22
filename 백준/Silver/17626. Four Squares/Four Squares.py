import sys
n=int(sys.stdin.readline())
dp=[i for i in range(n+1)]
x=1
while(x**2<=n):
    dp[x**2]=1
    x+=1
for i in range(2,n+1):
    y=1
    while(y**2<i):
        dp[i]=min(dp[i],1+dp[i-y**2])
        y+=1
print(dp[n])