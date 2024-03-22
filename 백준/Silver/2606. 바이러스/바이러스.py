import sys
t=int(sys.stdin.readline())
n=int(sys.stdin.readline())
d=[[]for i in range(t+1)]
def dfs(graph,start):
    visited =list()
    stack=list()
    stack.append(start)
    while stack:
        node=stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])
    print(len(visited)-1)
for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    d[a].append(b)
    d[b].append(a)
dfs(d,1)