n,k=map(int,input().split())
l=[i for i in range(1,n+1)]
ans=[]
size=n
front=0
rear=n-1
while(size>0):
    cur=(front+k-1)%size
    ans.append(l.pop(cur))
    size-=1
    if(size==0):
        break
    front=cur%size
print("<",end='')
for i in range(n-1):
    print(ans[i],end=', ')
print(ans[n-1],end='>\n')