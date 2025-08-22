from collections import deque
def bfs(a, n, graph):
    q=deque([a])
    count=1
    visited=[False for _ in range(n+1)]
    visited[a]= True
    while(q):
        cur= q.popleft()
        for next in graph[cur]:
            if(visited[next]==False):
                visited[next]= True
                q.append(next)
                count+=1
    return count
                
def solution(n, results):
    answer= 0
    win  =[[] for _ in range(n+1)]
    lose =[[] for _ in range(n+1)]
    visited=[0 for _ in range(n+1)]
    for w, l in results:
        win[w].append(l)
        lose[l].append(w)
    for i in range(1,n+1):
        win_num= bfs(i,n,win)-1
        lose_num= bfs(i,n,lose)-1
        if(win_num+ lose_num== n-1):
            answer+=1
    
    return answer