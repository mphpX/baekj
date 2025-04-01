import sys
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
n,m=map(int,input().split())
num=sorted(list(set(list(map(int,input().split())))))
cir=[]
s=[]
ans=set()
def dfs(start):
    if(len(cir)==m):
        print(' '.join(map(str,cir)))
        return
    for i in range(start,len(num)):
        cir.append(num[i])
        dfs(i)
        cir.pop()
dfs(0)