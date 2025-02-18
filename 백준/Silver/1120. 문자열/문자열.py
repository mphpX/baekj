a,b=list(input().split())
def acc(a,b):
    ct=0
    for i in range(len(a)):
        if(a[i]!=b[i]):
            ct+=1
    return ct
ans=[]
for i in range(len(b)-len(a)+1):
    ans.append(acc(a,b[i:i+len(a)]))
print(min(ans))