a,b,c=map(int,input().split())
l=[0 for i in range(100)]
for i in range(1,a+1):
    for j in range(1,b+1):
        for k in range(1,c+1):
            l[i+j+k]+=1
ct=0
mx=0
for i in range(3,a+b+c+1):
    if(l[i]>mx):
        ct=i
        mx=l[i]
print(ct)