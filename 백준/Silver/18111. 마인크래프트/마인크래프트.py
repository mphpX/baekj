import sys
n,m,b=map(int,sys.stdin.readline().split())
l=[]
mn=256
mx=0
time=48000000
h=0
for i in range(n):
    a=list(map(int,sys.stdin.readline().split()))
    l.append(a)
    mx=max(max(a),mx)
    mn=min(min(a),mn)
for i in range(mn,mx+1):
    ctime=0
    cblock=b
    for j in range(n):
        for k in range(m):
            if(l[j][k]>i):
                ctime+=2*(l[j][k]-i)
                cblock+=l[j][k]-i
            else:
                ctime+=i-l[j][k]
                cblock-=i-l[j][k]        
    if(cblock>=0):
        if(time>=ctime):
            time=ctime
            h=i
    else:
        break
print(time,h)