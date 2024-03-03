import sys
n = int(sys.stdin.readline())
l=[]
for i in range(n):
    a=list(map(int,sys.stdin.readline().split()))
    l.append(a)
l.sort(key=lambda x : (x[0],x[1]))
end=0
start=0
ct=0
for i in range(n):
    if(l[i][1]>=end):
        if(l[i][0]>=end):
            ct+=1
            end=l[i][1]
    else:
        start=l[i][0]
        end=l[i][1]
print(ct)