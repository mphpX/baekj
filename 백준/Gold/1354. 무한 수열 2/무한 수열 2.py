n,p,q,x,y=map(int,input().split())
d=dict()
d[0]=1
def solve(n,a,b,w,z):
    if(n in d):
        return d[n]
    if(n<=0):
        return 1
    d[n]=solve(n//a-w,a,b,w,z)+solve(n//b-z,a,b,w,z)
    return d[n]
print(solve(n,p,q,x,y))