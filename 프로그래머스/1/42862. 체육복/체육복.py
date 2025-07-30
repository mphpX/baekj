def solution(n, lost, reserve):
    shirts=[1 for _ in range(n+1)]
    shirts[0]=0
    for i in lost:
        shirts[i]-=1
    for i in reserve:
        shirts[i]+=1
    noshirts=[]
    for i in range(1,n+1):
        if(shirts[i]==0):
            noshirts.append(i)
    ct=len(noshirts)
    dx=[-1,1]
    for i in noshirts:
        for j in dx:
            if(1<=i+j <=n):
                if(shirts[i+j]==2):
                    shirts[i+j]-=1
                    shirts[i]+=1
                    ct-=1
                    break
    return n-ct