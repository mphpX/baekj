a,b=map(int,input().split())
l=[i for i in range(100)]
for i in range(1,100):
    l[i]+=l[i-1]
ans=[]
while(b-1<100):
    if((a-l[b-1])%b==0 and (a-l[b-1])//b>=0):
        s=(a-l[b-1])//b
        for i in range(b):
            ans.append(s+i)
        break
    b+=1
if(len(ans)==0):
    print(-1)
else: 
    for i in ans:
        print(i, end=' ')