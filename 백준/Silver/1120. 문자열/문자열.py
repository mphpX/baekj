a,b=map(str,input().split())
a=list(a)
b=list(b)
def acc(a,b):
    ct=0
    for i in range(len(a)):
        if(a[i]!=b[i]):
            ct+=1
    return ct
ans=len(b)
for i in range(len(b)-len(a)+1):
    ans=min(ans,acc(a,b[i:i+len(a)]))
print(ans)