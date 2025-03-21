import sys
input = sys.stdin.readline
n = int(input())
st = [0 for _ in range(n)]
for i in range(n):
    x = int(input())
    st[i] = x
dp= [0 for _ in range(n)]
dp[0]=st[0]
if(n>1):
    dp[1]=st[0]+st[1]
    if(n>2):
        dp[2]=max(st[0],st[1])+st[2]
for i in range(3,n):
    dp[i]=max(dp[i-2],dp[i-3]+st[i-1],dp[i-1]-st[i-1])+st[i]
print(dp[n-1])