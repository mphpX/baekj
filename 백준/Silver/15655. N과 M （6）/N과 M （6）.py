import sys
input= sys.stdin.readline
n,m=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
visited=[False for _ in range(len(l))]
def back_track(a,result):
    if(len(result)==m):
        for i in result:
            print(i,end=' ')
        print()
        return
    for i in range(a,len(l)):
        if(visited[i]==False):
            visited[i]=True
            back_track(i,result+[l[i]])
            visited[i]=False
back_track(0,[])