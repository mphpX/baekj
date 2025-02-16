n,m=map(int,input().split())
l=[]
dp=[[0 for i in range(n+1)]for j in range(m+1)]

for i in range(n):
    a,b=map(int,input().split())
    #a-> weight b-> k
    l.append([a,b])
for i in range(1,m+1):
    for j in range(1,n+1):
        weight,value=l[j-1]
        if(i>=weight):
            dp[i][j]=max(dp[i-weight][j-1]+value,dp[i][j-1])
        else:
            dp[i][j]=dp[i][j-1]
print(dp[m][n])
