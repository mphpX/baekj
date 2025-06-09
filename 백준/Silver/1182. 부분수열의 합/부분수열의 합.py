import sys
input= sys.stdin.readline
n,m=map(int,input().split())
arr=list(map(int,input().split()))
ans=0
def back_track(s,cur,l):
    if(cur==n):
        if(s==m and l>0):
            global ans
            ans+=1
        return
    back_track(s+arr[cur],cur+1,l+1)
    back_track(s,cur+1,l)
back_track(0,0,0)
print(ans)