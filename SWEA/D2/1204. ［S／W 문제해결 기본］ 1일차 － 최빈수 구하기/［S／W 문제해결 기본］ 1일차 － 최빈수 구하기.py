T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    t= int(input())
    graph= [0 for _ in range(101)]
    arr= list(map(int,input().split()))
    for num in arr:
        graph[num]+=1
    mx= max(graph)
    for i in range(100,-1,-1):
        if(graph[i] == mx):
            print('#',t,' ', i, sep='')
            continue