n,m= map(int,input().split())
graph=[]
for i in range(n):
    l= input().strip()
    graph.append(list(map(int, str(l))))
ans=-1
for i in range(n):
    for j in range(m):
        for dx in range(-n,n):
            for dy in range(-m,m):
                if(dx==0 and dy==0):
                    continue
                num=0
                x=i
                y=j
                while(0<=x<n and 0<=y<m):
                    num=num*10+graph[x][y]
                    if(ans<num):
                        rt=num**(1/2)
                        if(rt==int(rt)):
                            ans=num
                    x+=dx
                    y+=dy
print(ans)