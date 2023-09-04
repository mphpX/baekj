import sys
n=int(input())

dp=[0,0,1]

for i in range(3,n+1):
    if(i%3==0 and i%2==0):
        dp.append(min(dp[i//2],dp[i//3],dp[i-1])+1)
    elif(i%3==0):
        dp.append(min(dp[i//3],dp[i-1])+1)
    elif(i%2==0):
        dp.append(min(dp[i//2],dp[i-1])+1)
    else:
        dp.append(dp[i-1]+1)
print(dp[n])
print(n,end=" ")
while(n!=1):
    if(n%3==0 and n%2==0):
        m=min(dp[n//2],dp[n//3],dp[n-1])
        if(m==dp[n//3]):n=n//3
        elif(m==dp[n//2]):n=n//2
        else:n=n-1
    elif(n%3==0):
        m=min(dp[n//3],dp[n-1])
        if(m==dp[n//3]):n=n//3
        else:n=n-1
    elif(n%2==0):
        m=min(dp[n//2],dp[n-1])
        if(m==dp[n//2]):n=n//2
        else:n=n-1
    else:
        n=n-1
    print(n,end=" ")