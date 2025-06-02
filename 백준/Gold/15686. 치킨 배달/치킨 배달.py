import sys
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]
chick=[]
house=[]

for i in range(n):
    for j in range(n):
        if(graph[i][j]==2):
            chick.append((i,j))
        elif(graph[i][j]==1):
            house.append((i,j))
cross=[[0 for _ in range(len(house))] for _ in range(len(chick))]
ok=[]
for i in range(len(chick)):
    c_x,c_y=chick[i]
    for j in range(len(house)):
        h_x,h_y=house[j]  
        cross[i][j]= abs(h_x-c_x)+ abs(h_y-c_y)

def back_track(x,left):
    if(len(left)==m):
        ok.append(left)
        return
    for i in range(x,len(chick)):
        back_track(i+1,left+[i])
back_track(0,[])

ans=500000
for i in range(len(ok)):
    compare=0
    for j in range(len(house)):
        plus=50000
        for k in range(m):
            plus=min(plus,cross[ok[i][k]][j])
        compare+=plus
    ans=min(ans,compare)
print(ans)