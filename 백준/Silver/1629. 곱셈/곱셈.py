import sys
sys.setrecursionlimit(10**6)
n,m,o=map(int,sys.stdin.readline().split())
def fpow(c,p):
    if p==1:
        return c%o
    else:
        x=fpow(c,p//2)
        if p%2==0:
            return (x*x)%o
        else:
            return (x*x*c)%o
print(fpow(n,m))
