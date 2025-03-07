ans=[]
for i in range(7):
    a=int(input())
    if(a%2==1):
        ans.append(a)
ans.sort()
if(len(ans)==0):
    print(-1)
else:
    print(sum(ans))
    print(ans[0])