import sys
input=sys.stdin.readline
n,m,r=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]
mn=min(n,m)
reversed=[[] for _ in range(mn//2)]
r_graph=[[0 for _ in range(m)] for _ in range(n)]
for i in range(mn//2):    
    for j in range(0+i,m-i):
        reversed[i].append(graph[i][j])
    for j in range(1+i,n-i):
        reversed[i].append(graph[j][m-1-i])
    for j in range(m-2-i,-1+i,-1):
        reversed[i].append(graph[n-1-i][j])
    for j in range(n-2-i,0+i,-1):
        reversed[i].append(graph[j][i])
for i in range(mn//2):
    ct=0
    for j in range(0+i,m-i):
        r_graph[i][j]= reversed[i][(ct+r)%len(reversed[i])]
        ct+=1
    for j in range(1+i,n-i):
        r_graph[j][m-1-i]= reversed[i][(ct+r)%len(reversed[i])]
        ct+=1
    for j in range(m-2-i,-1+i,-1):
        r_graph[n-1-i][j]= reversed[i][(ct+r)%len(reversed[i])]
        ct+=1
    for j in range(n-2-i,0+i,-1):
        r_graph[j][i]= reversed[i][(ct+r)%len(reversed[i])]
        ct+=1
for i in range(n):
    for j in range(m):
        print(r_graph[i][j],end=' ')
    print()