import sys
input=sys.stdin.readline
n=int(input())
graph=[list(map(int,input().split())) for _ in range(n)]
team=n//2
nums=[i for i in range(1,n+1)]
ft=[]
visited=[False for _ in range(n+1)]
def dfs(x,t):
    if(len(x)==t):
        ft.append(list(x))
        return
    s=1
    if(len(x)!=0):
        s=x[len(x)-1]
    for i in range(s,t*2):
        if(visited[i]==False):
            visited[i]=True
            x.append(i)
            dfs(x,t)
            x.pop()
            visited[i]=False
ex=[]
dfs(ex,team)
st=[list(set(nums)-set(ft[i])) for i in range(len(ft))]
ans=1000000
for i in range(len(ft)):
    ftans=0
    stans=0
    for j in range(team):
        for k in range(j,team):
            ftans+=graph[ft[i][j]-1][ft[i][k]-1]+graph[ft[i][k]-1][ft[i][j]-1]
            stans+=graph[st[i][j]-1][st[i][k]-1]+graph[st[i][k]-1][st[i][j]-1]
    candy=ftans-stans
    if(candy<0):
        candy=-candy
    if(candy<ans):
        ans=candy
print(ans)    
