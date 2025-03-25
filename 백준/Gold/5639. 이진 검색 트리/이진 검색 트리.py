import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
preorder=[]
n=0
while(True):
    try:
        data=int(input())
        preorder.append(data)
        n+=1
    except:
        break
ans=[]
def postorder(li,start,end):
    if(start>end):
        return
    root=li[start]
    mid=start+1
    while(mid<=end and root>li[mid]):
        mid+=1
    postorder(li,start+1,mid-1)
    postorder(li,mid,end)
    ans.append(li[start])
    
postorder(preorder,0,n-1)
for i in ans:
    print(i)