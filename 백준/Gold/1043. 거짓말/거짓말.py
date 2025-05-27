import sys
from collections import deque
input= sys.stdin.readline

n,m= map(int,input().split())
truth=list(map(int,input().split()))
party=[]
where=[[] for _ in range(n+1)]
for i in range(m):
    party.append(list(map(int,input().split())))
    for j in range(1,party[i][0]+1):
        where[party[i][j]].append(i)
visited_party=[0 for _ in range(m)]
def bfs():
    q=deque(truth[1:])
    visited=[0 for _ in range(n+1)]
    for i in truth[1:]:
        visited[i]=1
    while(q):
        cur=q.popleft()
        for next_party in where[cur]:
            if(visited_party[next_party]==0):
                visited_party[next_party]=1
                for j in party[next_party][1:]:
                    if(visited[j]==0):
                        visited[j]=1
                        q.append(j)
    return
bfs()
print(m-sum(visited_party))