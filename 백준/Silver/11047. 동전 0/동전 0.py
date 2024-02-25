import sys
n,m=map(int,sys.stdin.readline().split())
l=[0 for i in range(n)]
for i in range(n):
    l[i]=int(sys.stdin.readline())
ct=0
o=n-1
while(m):
    if(m//l[o]>0):
        ct+=m//l[o]
        m-=m//l[o]*l[o]
    o-=1
print(ct)