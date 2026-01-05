def rotate(graph, n):
    rotate_graph = []
    for i in range(n):
        arr=[]
        for j in range(n-1,-1,-1):
            arr.append(graph[j][i])
        rotate_graph.append(arr)
    return rotate_graph
T = int(input())
for test_case in range(1, T + 1):
    n, m= map(int,input().split())
    a= list(map(int,input().split()))
    b= list(map(int,input().split()))
    r= min(n,m)
    limit= max(n,m) 
    ans=0
    if(n>m):
        a, b= b, a
    for i in range(limit - r+1):
        ans= max(ans,sum([a[j]* b[i+j] for j in range(r)]))
    print('#', test_case, ' ', ans, sep='')