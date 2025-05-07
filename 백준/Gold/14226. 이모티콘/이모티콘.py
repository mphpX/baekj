from collections import deque
s=int(input())
visited=[[-1 for _ in range(2001)] for _ in range(2001)]
def bfs(start,end):
    q=deque([(start,0)])
    visited[start][0]=0
    while(q):
        cur,copy=q.popleft()
        if cur == end:
            print(visited[cur][copy])
            break
        if(visited[cur][cur]==-1):
            visited[cur][cur]=visited[cur][copy]+1
            q.append((cur,cur))
        if(cur+copy<2001 and visited[cur+copy][copy]==-1):
            visited[cur+copy][copy]=visited[cur][copy]+1
            q.append((cur+copy,copy))
        if(2<=cur-1 and visited[cur-1][copy]==-1):
            visited[cur-1][copy]=visited[cur][copy]+1
            q.append((cur-1,copy))
bfs(1,s)