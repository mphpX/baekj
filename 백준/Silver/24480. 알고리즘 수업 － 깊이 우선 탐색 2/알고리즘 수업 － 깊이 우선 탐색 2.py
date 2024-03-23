import sys
sys.setrecursionlimit(10**9)
n,m,o=map(int,sys.stdin.readline().split())
l=[[] for i in range(n+1)]
visited=[0 for i in range(n+1)]
x=[0 for i in range(n+1)]
ct=1
def dfs(graph,start):
    global ct
    x[start]=ct
    ct+=1
    visited[start]=1
    for i in graph[start]:
        if not visited[i]:
            dfs(graph,i)

for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    l[a].append(b)
    l[b].append(a)
for i in l:
    i.sort(reverse=True)
dfs(l,o)
for i in range(1,len(x)):
    print(x[i])