n,p,q=map(int,input().split())
d=dict()
d[0]=1
def solve(n,a,b):
    if(n in d):
        return d[n]
    d[n]=solve(n//a,a,b)+solve(n//b,a,b)
    return d[n]
print(solve(n,p,q))