import sys
import heapq
input=sys.stdin.readline
n=int(input().strip())
m=int(input().strip())
graph=[[] for _ in range(1001)]
for i in range(m):
    start,end,cost=map(int,input().split())
    graph[start].append((end,cost))
origin,destination=map(int,input().split())
ans=[100000*m for _ in range(n+1)]
visited=[False for _ in range(n+1)]
ans[0]=0
ans[origin]=0
cur=origin
pq = []
heapq.heappush(pq, (0, origin))
while(pq):
    cost, cur=heapq.heappop(pq)
    if(cost>ans[cur]):
        continue
    for i in graph[cur]:
        if(i[1]+cost<ans[i[0]]):
            ans[i[0]]=i[1]+cost
            heapq.heappush(pq, (i[1]+cost,i[0]))
print(ans[destination])