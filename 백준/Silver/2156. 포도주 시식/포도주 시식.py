n=int(input())
wine=[]
for i in range(n):
    a=int(input())
    wine.append(a)
dp=[0 for i in range(n)]
dp[0]=wine[0]
if(n>1):
    dp[1]=wine[0]+wine[1]
    if(n>2):
        dp[2]=max(dp[1],wine[1]+wine[2])

for i in range(3,n):
    dp[i]=max(dp[i-2]+wine[i],dp[i-2]-wine[i-2]+wine[i-1]+wine[i],dp[i-3]+wine[i-1]+wine[i])
print(max(dp))