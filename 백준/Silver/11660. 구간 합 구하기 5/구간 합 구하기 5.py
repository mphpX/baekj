import sys
input=sys.stdin.readline
n,t=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]
dp=graph
for i in range(n):
    for j in range(n):
        if(j==0):
            continue   
        dp[i][j]+=dp[i][j-1]
for i in range(1,n):
    for j in range(n):
        dp[i][j]+=dp[i-1][j]        
for _ in range(t):
    fx,fy, sx,sy=map(int,input().split())
    fx,fy, sx,sy = fx-1,fy-1, sx-1,sy-1
    l,ll,lll=0,0,0
    if(fy!=0):
        l=dp[sx][fy-1]
    if(fx!=0):
        ll=dp[fx-1][sy]
    if(fy!=0 and fx!=0):
        lll=dp[fx-1][fy-1]
    ans=dp[sx][sy]-l-ll+lll
    print(ans)