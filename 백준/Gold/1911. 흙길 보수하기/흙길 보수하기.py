n,l = map(int,input().split())
start=[]
end=[]
for i in range(n):
    s,e=map(int,input().split())
    start.append(s)
    end.append(e)
start.sort()
end.sort()
ct=(end[0]-start[0]+l-1)//l
cur=start[0]+(end[0]-start[0]+l-1)//l*l
for i in range(1,n):
    s=start[i]
    if(cur>= s):
        s = cur
    ct+= (end[i]-s+l-1)//l
    cur=s+ (end[i]-s+l-1)//l*l
print(ct)