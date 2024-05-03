import sys
n=int(sys.stdin.readline())
ct=0
d=dict()
d['ChongChong']=1
for i in range(n):
    l=list(sys.stdin.readline().split())
    if(l[0] in d):
        if(l[1] not in d):
            d[l[1]]=1
    elif(l[1] in d):
        if (l[0] not in d):
            d[l[0]] = 1
for i in d:
    ct+=d[i]
print(ct)