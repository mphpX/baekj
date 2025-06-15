import sys
input=sys.stdin.readline
n=int(input())
chart=[]
d=dict()
for i in range(n):
    l=list(map(int,input().split()))
    for j in range(5):
        if(j*10+l[j] in d):
            d[j*10+l[j]].add(i)
        else:
            d[j*10+l[j]]=set([i])
    chart.append(l)
ans=[0 for _ in range(n)]

for i in range(n):
    first= set(d[chart[i][0]])
    for j in range(1,5):
        first |=d[j*10+chart[i][j]]
    ans[i]=len(first)
mx=0
idx=0
for i in range(n):
    if(mx<ans[i]):
        mx=ans[i]
        idx=i
print(idx+1)