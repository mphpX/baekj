import sys
input=sys.stdin.readline
n=int(input())
l=list(input().split())
visited=[False for _ in range(10)]
ans=[]
ans_list=[]
def dfs(ct):
    if(ct==n+1):
        ans_list.append(list(ans))
        return
    for i in range(10):
        if(ct==0):
            ans.append(i)
            visited[i]=True
            dfs(ct+1)
            ans.pop()
            visited[i]=False
        else:
            if(l[ct-1]=='<'):
                if(visited[i]==False and i > ans[ct-1]):
                    ans.append(i)
                    visited[i]=True
                    dfs(ct+1)
                    ans.pop()
                    visited[i]=False
            else:
                if(visited[i]==False and i < ans[ct-1]):
                    ans.append(i)
                    visited[i]=True
                    dfs(ct+1)
                    ans.pop()
                    visited[i]=False
dfs(0)
for i in ans_list[len(ans_list)-1]:
    print(i,end='')
print()
for i in ans_list[0]:
    print(i,end='')
print()