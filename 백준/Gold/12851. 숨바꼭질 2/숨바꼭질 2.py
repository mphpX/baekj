from collections import deque
n,k=map(int,input().split())
ans=[200001,1]
visited=[-1 for _ in range(200001)]
visited[n]=0
def bfs(a):
    q=deque([a])
    while(q):
        cur=q.popleft()
        if(cur==k):
            if(ans[0]>visited[cur]):
                ans[0]=visited[cur]
                ans[1]=1
            elif(ans[0]==visited[cur]):
                ans[1]+=1
            else:
                break
        next=[cur-1,cur+1,cur*2]
        for n_x in next:
            if(0<=n_x<200001):
                if(visited[n_x]==-1):
                    visited[n_x]=visited[cur]+1
                    q.append(n_x)
                elif(visited[n_x]==visited[cur]+1):
                    q.append(n_x)
bfs(n)
print(ans[0])
print(ans[1])