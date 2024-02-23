import sys
l=list(map(int,sys.stdin.readline().split()))
dp = [[[1 for _ in range(51)] for _ in range(51)] for _ in range(51)]
for i in range(1,51):
    for j in range(1,51):
        for k in range(1,51):
            if(max(i,j,k)>20):
                dp[i][j][k]=dp[20][20][20]
                dp[j][i][k]=dp[20][20][20]
                dp[k][j][i]==dp[20][20][20]
                dp[i][k][j]=dp[20][20][20]
                dp[j][k][i]=dp[20][20][20]
                dp[k][i][j]=dp[20][20][20]
            elif(i<j and j<k):
                dp[i][j][k]=dp[i][j][k-1]+dp[i][j-1][k-1]-dp[i][j-1][k]
            else:
                dp[i][j][k]=dp[i-1][j][k]+dp[i-1][j-1][k]+dp[i-1][j][k-1]-dp[i-1][j-1][k-1]

while(l[0]!=-1 or l[1]!=-1 or l[2]!=-1):
    print("w(",end="")
    print(l[0],l[1],l[2],sep=', ',end='')
    print(") = ",end='')
    if(min(l)<=0):
        print(1)
    else:
        print(dp[l[0]][l[1]][l[2]])
    l=list(map(int,sys.stdin.readline().split()))