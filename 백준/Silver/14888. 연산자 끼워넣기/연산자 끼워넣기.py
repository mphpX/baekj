import sys
input=sys.stdin.readline
n=int(input())
l=list(map(int,input().split()))
op=list(map(int,input().split()))
visited=[0 for _ in range(4)]
ans=[]
def dfs(cur,value):
    if(cur==n-1):
        ans.append(value)
        return
    next=[value+l[cur+1],value-l[cur+1],value*l[cur+1],value//l[cur+1]]
    if(value<0):
        next[3]=-(-value // l[cur+1])
    for i in range(4):
        if(op[i] > visited[i]):
            visited[i]+=1
            dfs(cur+1,next[i])
            visited[i]-=1
dfs(0,l[0])
print(max(ans),min(ans),sep='\n')