import sys
n=int(sys.stdin.readline())
l=[]
result=[1 for i in range(n)]
for i in range(n):
    x,y=map(int,sys.stdin.readline().split())
    l.append([x,y])
for i in range(n):
    for j in range(n):
        if(i!=j):
            if(l[i][0]<l[j][0] and l[i][1]<l[j][1]):
                result[i]+=1
for i in result:
    print(i,end=' ')