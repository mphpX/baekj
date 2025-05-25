import sys
input=sys.stdin.readline
n=int(input())
mxdp=[[0,0,0] for _ in range(2)]
mndp=[[10*n,10*n,10*n] for _ in range(2)]
dx=[-1,0,1]
graph=list(map(int,input().split()))

for i in range(3):
    mxdp[0][i]=graph[i]
    mndp[0][i]=graph[i]

for i in range(1,n):
    graph=list(map(int,input().split()))
    
    for l in range(3):
        mxdp[i%2][l]=0
        mndp[i%2][l]=10*n
    for j in range(3):
        for k in range(3):
            n_x=j+dx[k]
            if(0<=n_x<3):
                if(mxdp[i%2][j]< mxdp[(i-1)%2][n_x]+ graph[j]):
                    mxdp[i%2][j]=mxdp[(i-1)%2][n_x]+graph[j]
                
                if(mndp[i%2][j]> mndp[(i-1)%2][n_x]+ graph[j]):
                    mndp[i%2][j]=mndp[(i-1)%2][n_x]+graph[j]

print(max(mxdp[(n-1)%2]),min(mndp[(n-1)%2]))