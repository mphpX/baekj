from collections import deque
n,m=map(int,input().split())
l=list(map(int,input().split()))
num=deque([i for i in range(1,n+1)])
cur=0
ans=0
for i in l:
    ct=0
    cur=0
    while(num[cur]!=i):
        ct+=1
        cur=(cur+1)%n
    ans+=min(ct,n-ct)
    num.rotate(-ct)
    num.popleft()
    n-=1
print(ans)