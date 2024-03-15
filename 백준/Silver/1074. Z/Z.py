import sys
n,r,c=map(int,sys.stdin.readline().split())
ct=0
def divide(p,x,y):
    global ct
    if x>r or x+p <=r or y>c or y+p<=c:
        ct+=p**2
        return
    if p>2:
        q=p//2
        divide(q,x,y)
        divide(q,x,y+q)
        divide(q,x+q,y)
        divide(q,x+q,y+q)
    else:
        if x==r and y==c:
            print(ct)
        elif x==r and y+1==c:
            print(ct+1)
        elif x+1==r and y==c:
            print(ct+2)
        else:
            print(ct+3)
        return
divide(2**n,0,0)