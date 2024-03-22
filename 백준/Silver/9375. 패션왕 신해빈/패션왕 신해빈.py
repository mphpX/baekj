import sys
t=int(sys.stdin.readline())
for i in range(t):
    n=int(sys.stdin.readline())
    d=dict()
    ct=1
    for j in range(n):
        l=list(sys.stdin.readline().split())
        if(l[1] in d):
            d[l[1]]+=1
        else:
            d[l[1]]=1
    for j in d:
        ct*=(d[j]+1)
    print(ct-1)