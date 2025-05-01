from heapq import heappop, heappush
import sys
input=sys.stdin.readline
hv,e=map(int,input().split())
graph=[[] for _ in range(hv+1)]
for i in range(e):
    u,v,w=map(int,input().split())
    graph[u].append((w,v))
    graph[v].append((w,u))

def dikstra(v):
    heap=[(0,v)]
    seen=set()
    d=[float('inf') for _ in range(hv+1)]
    d[v]=0
    while(heap):
        _, cur= heappop(heap)
        if cur in seen:
            continue
        seen.add(cur)
        for weight,next in graph[cur]:
            if(d[cur]+weight<d[next]):
                d[next]=d[cur]+weight
                heappush(heap,(d[next],next))
    return d
dp=[]
a,b=map(int,input().split())
dp.append(dikstra(1))
dp.append(dikstra(a))
dp.append(dikstra(b))
ans=min(dp[0][a]+dp[1][b]+dp[2][hv],dp[0][b]+dp[2][a]+dp[1][hv])
if(ans==float('inf')):
    ans=-1
print(ans)