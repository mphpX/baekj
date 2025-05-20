import sys
input=sys.stdin.readline
n,m,k=map(int,input().split())
graph=[list(input().strip()) for _ in range(n)]
dp=[[[0 for _ in range(m)] for _ in range(n)]for _ in range(2)]
bf=[['B','W'],['W','B']]
if(dp[0][0][0]!='B'):
    dp[0][0][0]=1
if(dp[1][0][0]=='B'):
    dp[1][0][0]=1

for i in range(n):
    for j in range(m):
        if(i==0 and j==0):
            continue
        if(graph[i][j]!=bf[i%2][j%2]):
            dp[0][i][j]+=1
        else:
            dp[1][i][j]+=1
        fpi, fpj, fmij=0, 0, 0
        spi, spj, smij=0, 0, 0
        if(i>=1):
            fpi=dp[0][i-1][j]
            spi=dp[1][i-1][j]
        if(j>=1):
            fpj=dp[0][i][j-1]
            spj=dp[1][i][j-1]
        if(i>=1 and j>=1):
            fmij=dp[0][i-1][j-1]
            smij=dp[1][i-1][j-1]
        dp[0][i][j]+=fpi+fpj-fmij
        dp[1][i][j]+=spi+spj-smij
mn=min(dp[0][k-1][k-1],dp[1][k-1][k-1])

for i in range(k-1,n):
    for j in range(k-1,m):
        if(i-k+1==0 and j-k+1==0):
            continue
        fpi, fpj, fmij=0, 0, 0
        spi, spj, smij=0, 0, 0
        if(i-k>=0):
            fpi=dp[0][i-k][j]
            spi=dp[1][i-k][j]
        if(j-k>=0):
            fpj=dp[0][i][j-k]
            spj=dp[1][i][j-k]
        if(i-k>=0 and j-k>=0):
            fmij=dp[0][i-k][j-k]
            smij=dp[1][i-k][j-k]
        mn=min(mn, dp[0][i][j]-(fpi+fpj-fmij), dp[1][i][j]- (spi+spj-smij))
print(mn)
