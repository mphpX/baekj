def solution(babbling):
    dataset=["aya", "ye", "woo", "ma"]
    s=[]
    ans=[]
    def dfs(m):
        if(len(s)==m):
            ans.append(list(s))
            return
        for i in range(4):
            if i not in s:
                s.append(i)
                dfs(m)
                s.pop()
    for i in range(1,5):
        s=[]
        dfs(i)
    
    answer = 0
    for i in ans:
        a=""
        for j in i:
            a+=dataset[j]
        for j in babbling:
            if(a==j):
                answer+=1
    
    return answer