import sys
from collections import deque
input=sys.stdin.readline
n,k=map(int,input().split())
visited=[[0,0] for _ in range(200001)]
ans=[]
def bfs(a,b):
    q=deque([a])
    visited[a][0]=-1
    visited[a][1]=1
    while(q):
        cur=q.popleft()
        if(cur==b):
            break
        l=[cur-1,cur+1,cur*2]
        for i in l:
            if(0<=i<200001 and visited[i][1]==0):
                visited[i][0]=cur
                visited[i][1]=visited[cur][1]+1
                q.append(i)
            if(cur>b):
                break
bfs(n,k)
x=k
while(visited[x][0]!=-1):
    ans.append(x)
    x=visited[x][0]
print(visited[k][1]-1)
print(n,end=' ')
for i in range(len(ans)-1,-1,-1):
    print(ans[i],end=' ')