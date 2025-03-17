n,m=map(int,input().split())
graph=[]
for i in range(n):
    a=input()
    graph.append(a)
x=set([i for i in range(n)])
y=set([i for i in range(m)])
for i in range(n):
    for j in range(m):
        if(graph[i][j]=='X'):
            if i in x:
                x.remove(i)
            if j in y:
                y.remove(j)
print(max(len(x),len(y)))