a,b=map(int,input().split())
l=[0 for _ in range(1001)]
d=1
idx=1
std=1
ct=0
while(idx<1001):
    if(ct<std):
        l[idx]=std
        idx+=1
        ct+=1
    else:
        ct=0
        std+=1
print(sum(l[a:b+1]))