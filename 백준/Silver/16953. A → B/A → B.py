from collections import deque
a,b=map(int,input().split())
def bfs(a,b):
    q=deque([(a,1)])
    while(q):
        cur,ct=q.popleft()
        if(cur==b):
            return ct
        if cur * 2 <= b:
            q.append((cur * 2, ct + 1))
        if cur * 10 + 1 <= b:
            q.append((cur * 10 + 1, ct + 1))
    return -1
print(bfs(a,b))