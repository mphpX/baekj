import sys    
n,m=map(int,sys.stdin.readline().split())
l=[]
for i in range(n):
    a=int(sys.stdin.readline())
    l.append(a)
end=sum(l)
start=1
ct=0
a=[]
while(start<=end):
    mid=(start+end)//2
    ct=0
    for i in l:
        ct+=i//mid
    if(ct>=m):
        a.append(mid)
        start=mid+1
    else:
        end=mid-1
print(max(a))