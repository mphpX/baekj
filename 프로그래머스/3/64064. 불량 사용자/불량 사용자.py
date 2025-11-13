def solution(user_id, banned_id):
    sl= [[] for _ in range(9)] 
    for uid in user_id:
        sl[len(uid)].append(uid)
    candidate=[[] for _ in range(len(banned_id))]
    for i in range(len(banned_id)):
        bid= banned_id[i]
        for uid in sl[len(bid)]:
            no=0
            for j in range(len(bid)):
                if(uid[j]==bid[j] or bid[j]=='*'):
                    continue
                else:
                    no=1
                    break
            if(no==0):
                candidate[i].append(uid)
    graph= dict()
    for uid in user_id:
        graph[uid]=0
    cases= set()
    def dfs(idx, picked):
        if(idx==len(candidate)):
            cases.add(tuple(sorted(picked)))
            return
        for ban in candidate[idx]:
            if(graph[ban]==0):
                graph[ban]=1
                dfs(idx+1, picked+[ban])
                graph[ban]=0
    dfs(0,[])
    return len(cases)