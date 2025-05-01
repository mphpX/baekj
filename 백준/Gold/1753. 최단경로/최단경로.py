from heapq import heappop, heappush
import sys
input=sys.stdin.readline

hv,e=map(int,input().split())
graph=[[] for _ in range(hv+1)]
k=int(input())
for i in range(e):
    u,v,w=map(int,input().split())
    graph[u].append((w,v))

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
ans=dikstra(k)
for i in range(1,hv+1):
    if(ans[i]==float('inf')):
        print('INF')
    else:
        print(ans[i])