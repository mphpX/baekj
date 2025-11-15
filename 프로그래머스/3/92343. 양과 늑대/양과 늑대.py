import sys
sys.setrecursionlimit(10**9)
answer = 0
def solution(info, edges):
    n= len(info)
    graph=[[] for _ in range(n)]
    for i,j in edges:
        graph[i].append(j)

    visited=[0 for _ in range(n)]
    candidates=[]
    sheep, wolf = 0, 0
    def dfs(sheep, wolf, candidates):
        global answer
        answer= max(sheep, answer)
        for i, node in enumerate(candidates):
            ns= sheep + (info[node]==0)
            nw= wolf + (info[node]==1)
            if(nw >= ns):
                continue
            next_candidates= candidates.copy()
            next_candidates.pop(i)
            visited[node]=1
            for ch in graph[node]:
                if(visited[ch]==0):
                    next_candidates.append(ch)
            dfs(ns,nw, next_candidates)
            visited[node]=0
    dfs(0,0, [0])
        
                
                
    return answer