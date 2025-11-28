T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, k = map(int,input().split())
    row= [0 for _ in range(n)]
    column= [0 for _ in range(n)]
    graph = [list(map(int,input().split())) for _ in range(n)]
    ans=0
    for i in range(n):
        x=0
        for j in range(n):
            if(graph[i][j]==1):
                x+=1
                if(j==n-1 and x== k):
                    ans+=1
            else:
                if(k==x):
                    ans+=1
                x=0
    for j in range(n):
        y = 0
        for i in range(n):
            if(graph[i][j]==1):
                y+=1
                if(i==n-1 and y==k):
                    ans+=1
            else:
                if(k==y):
                    ans+=1
                y=0
    print('#',test_case,' ', ans, sep='')