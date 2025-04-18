from collections import deque
n,k=map(int,input().split())
def bfs(start,end):
    visited=[0 for i in range(100001)]
    visited[start]=1
    q=deque([start])
    while(q):
        cur=q.popleft()
        if(cur==end):
            return visited[cur]
        tel=cur*2
        if(0<=tel<=100001 and visited[tel]==0):
            q.append(tel)
            visited[tel]=visited[cur]
        for i in [cur-1,cur+1]:
            if (0<=i<100001 and visited[i]==0):
                q.append(i)
                visited[i]=visited[cur]+1
        

print(bfs(n,k)-1)