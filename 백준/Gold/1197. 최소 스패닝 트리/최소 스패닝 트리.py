from queue import PriorityQueue
que = PriorityQueue()
v,e=map(int,input().split())
graph=[[] for _ in range(v+1)]
for i in range(e):
    x,y,c=map(int,input().split())
    graph[x].append((y,c))
    graph[y].append((x,c))
visit=[False for _ in range(v+1)]
ans=0
for i in graph[1]:
    que.put((i[1],1,i[0]))
visit[1]=True
while(not que.empty()):
    c,curv,nextv=que.get()
    if(visit[nextv]==True):
        continue
    ans+=c
    visit[nextv]=True
    for i in graph[nextv]:
        que.put((i[1],nextv,i[0]))
print(ans)