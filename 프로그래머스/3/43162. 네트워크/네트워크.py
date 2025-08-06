from collections import deque
def solution(n, computers):
    answer= 0
    visited=[False for _ in range(n)]
    for i in range(n):
        if(visited[i]==False):
            visited[i]=True
            q=deque([i])
            while(q):
                c_x=q.popleft()
                for n_x in range(n):
                    if(c_x==n_x):
                        continue
                    if(computers[c_x][n_x]==1 and visited[n_x]==False):
                        q.append(n_x)
                        visited[n_x]= True
            answer+=1
    return answer