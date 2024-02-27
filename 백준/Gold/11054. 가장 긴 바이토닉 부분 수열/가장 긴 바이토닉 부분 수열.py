n=int(input())
l=list(map(int,input().split()))
m=l[::-1]
pdp=[1 for i in range(n)]
mdp=[1 for i in range(n)]
for i in range(1,n):
    for j in range(i):
        if(l[i]>l[j]):
            pdp[i]=max(pdp[i],pdp[j]+1)
for i in range(1,n):
    for j in range(i):
        if(m[i]>m[j]):
            mdp[i]=max(mdp[i],mdp[j]+1)
result=0
for i in range(n):
    if(pdp[i]+mdp[n-i-1]-1>result):
        result=pdp[i]+mdp[n-i-1]-1
print(result)