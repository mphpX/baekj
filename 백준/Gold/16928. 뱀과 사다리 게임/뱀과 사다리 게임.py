n,m=map(int,input().split())
graph=[i for i in range(101)]
num=[0 for i in range(101)]
dp=[[] for i in range(18)]
dp[0].append(1)
for i in range(n):
    u,p=map(int,input().split())
    graph[u]=p
for i in range(m):
    do,wn=map(int,input().split())
    graph[do]=wn
ct=0
for i in range(1,18):
    for j in dp[i-1]:
        for k in range(1,7):
            if(j+k<101 and num[graph[j+k]]==0):
                dp[i].append(graph[j+k])
                num[graph[j+k]]=1
    if(100 in dp[i]):
        ct=i
        break
print(ct)