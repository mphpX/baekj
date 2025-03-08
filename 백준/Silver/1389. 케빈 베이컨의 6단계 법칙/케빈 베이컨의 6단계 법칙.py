from collections import deque
n,m=map(int,input().split())
rel=[[] for i in range(n+1)]
def bfs(n,x):
    visit=set()
    ans=[0 for i in range(n+1)]
    q=deque()
    q.append(x)
    while(q):
        cur=q.popleft()
        ct=0
        if(cur not in visit):
            visit.add(cur)
            q.extend(rel[cur])
            for i in rel[cur]:
                if(i not in visit and ans[i]==0):
                    ans[i]=ans[cur]+1
    return sum(ans)
            
for i in range(m):
    a,b=map(int,input().split())
    rel[a].append(b)
    rel[b].append(a)
a=[]
mn=5000000
idx=0
for i in range(1,n+1):
    if(bfs(n,i)<mn):
        mn=bfs(n,i)
        idx=i

print(idx)