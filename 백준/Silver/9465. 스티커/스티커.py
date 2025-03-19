t=int(input())
for i in range(t):
    n=int(input())
    st=[]
    for j in range(2):
        a=list(map(int,input().split()))
        st.append(a)
    dp=[[0 for _ in range(n)]for _ in range(2)]
    dp[0][0]=st[0][0]
    dp[1][0]=st[1][0]
    if(n>1):
        dp[1][1]=st[0][0]+st[1][1]
        dp[0][1]=st[1][0]+st[0][1]
    for j in range(2,n):
        dp[0][j]=max(dp[1][j-1]+st[0][j],dp[1][j-2]+st[0][j])
        dp[1][j]=max(dp[0][j-1]+st[1][j],dp[0][j-2]+st[1][j])
    print(max(max(dp[0]),max(dp[1])))