n,m=map(int,input().split())
l=[0]+list(map(int,input().split()))
remainder=[[] for _ in range(m)]
for i in range(1,n+1):
    l[i]+=l[i-1]
    remainder[l[i]%m].append(i)
remain=len(remainder[0])
ans=remain+ remain*(remain-1)//2
for i in range(1,m):
    remain=len(remainder[i])
    ans+=remain*(remain-1)//2

print(ans)