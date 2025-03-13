n,m=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
l.append(0)
s=[]
def dfs(start):
    if(len(s)==m):
        print(' '.join(map(str,s)))
        return
    for i in range(len(l)):
        if l[i] not in s:
            s.append(l[i])
            if(i+1<len(l)):
                dfs(l[i+1])
            if(len(s)!=0):
                s.pop()
dfs(l[0])