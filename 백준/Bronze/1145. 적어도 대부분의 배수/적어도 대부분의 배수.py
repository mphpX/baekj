import sys
l=list(map(int,sys.stdin.readline().split()))
m=min(l)
while True:
    ct=0
    for i in l:
        if m%i==0:
            ct+=1
    if(ct>=3):
        break
    m+=1
print(m)