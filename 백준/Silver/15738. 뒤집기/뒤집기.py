n,k,m=map(int,input().split())
l=list(map(int,input().split()))
for x in range(m):
    i=int(input())
    if(i>0):
        if(i>=k):
            k=i-k+1
    else:
        if(k>n+i):
            k=2*n+1-k+i
print(k)