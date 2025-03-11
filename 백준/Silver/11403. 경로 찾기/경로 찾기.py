n=int(input())
graph=[]
for i in range(n):
    l=list(map(int,input().split()))
    graph.append(l)
answer=[[0 for i in range(n)]for j in range(n)]
visit=[0 for i in range(n)]
def dfs(start,x):
    if(visit[x]==1):
        return
    visit[x]=1
    for i in range(n):
        if(graph[x][i]==1):
            if(visit[i]==0):
                answer[start][i]=1
                dfs(start,i)
            elif(visit[i]==1 and start==i):
                answer[start][i]=1
for i in range(n):
    visit=[0 for i in range(n)]
    dfs(i,i)
for i in range(n):
    for j in answer[i]:
        print(j,end=' ')
    print()