import sys
n=int(sys.stdin.readline())
lx=list(map(int,sys.stdin.readline().split()))
ly=list(map(int,sys.stdin.readline().split()))
lx=sorted(lx)
ly=sorted(ly,reverse=True)
s=0
for i in range(n):
    s+=lx[i]*ly[i]
print(s)