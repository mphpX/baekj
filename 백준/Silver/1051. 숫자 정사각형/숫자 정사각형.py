import sys
n,m=map(int,sys.stdin.readline().split())
l=[]
x=min(n,m)-1
for i in range(n):
    a=list(sys.stdin.readline().strip())
    l.append(a)
result=0
while(x>0):
    for i in range(0,n-x):
        for j in range(0,m-x):
            if(l[i][j]==l[i][j+x] and l[i][j]==l[i+x][j] and l[i][j]==l[i+x][j+x]):
                result=1
                break
    if(result==1):
        break
    else:
        x-=1
print((x+1)**2)