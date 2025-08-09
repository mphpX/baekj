from collections import deque
def diff_count(a,b):
    count=0
    for i in range(len(a)):
        if(a[i]!=b[i]): count+=1
    return count

def solution(begin, target, words):
    visited=[0 for _ in range(len(words))]
    q=deque([])
    idx=-1
    for i in range(len(words)):
        if(words[i]==target):
            idx=i
        if(diff_count(begin, words[i])== 1):
            q.append(i)
            visited[i]=1
    if(idx==-1):
        return 0
    while(q):
        cur= q.popleft()
        for i in range(len(words)):
            if(diff_count(words[cur], words[i])== 1):
                if(visited[i]==0):
                    q.append(i)
                    visited[i]= visited[cur]+1
            
    return visited[idx]