import sys
o=int(sys.stdin.readline())
for i in range(o):
    k=int(sys.stdin.readline())
    n=int(sys.stdin.readline())
    l=[j for j in range(1,n+1)]
    for j in range(k):
        for x in range(1,n):
            l[x]+=l[x-1]
    print(l[n-1])