from collections import deque
t= int(input())
def bfs(x,y):
    visited = [False for _ in range(10000)]
    l=['D','S','L','R']
    q=deque([(x,"")])
    visited[x]=True
    while(q):
        cur,command=q.popleft()
        if(cur==y):
            return command
        next=[(cur*2)%10000,(cur-1+10000)%10000,(cur%1000)*10+cur//1000, (cur%10)*1000+cur//10]
        for i in range(4):
            if(visited[next[i]]==False):
                visited[next[i]]=True
                q.append((next[i],command+l[i]))

for i in range(t):
    a,b=map(int,input().split())
    ans=bfs(a,b)
    for i in ans:
        print(i,end='')
    print()