n,m=map(int,input().split())
l=list(map(int,input().split()))
ans=[]
s=[]
visited=[0 for i in range(n)]
def bfs():
    if(len(s)==m):
        ans.append(tuple(s))
        return
    for i in range(len(l)):
        if(visited[i]==0):
            s.append(l[i])
            visited[i]=1
            bfs()
            s.pop()
            visited[i]=0
bfs()
ans=list(sorted(set(ans)))
for i in range(len(ans)):
    for j in ans[i]:
        print(j,end=' ')
    print()