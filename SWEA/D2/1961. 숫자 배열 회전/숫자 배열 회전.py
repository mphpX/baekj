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
    n= int(input())
    graph= [list(map(int,input().split())) for _ in range(n)]
    once = rotate(graph, n)
    twice = rotate(once, n)
    thrice = rotate(twice, n)
    print('#',test_case, sep='')
    for i in range(n):
        print("".join(map(str, once[i])), end=' ')
        print("".join(map(str, twice[i])), end=' ')
        print("".join(map(str, thrice[i])))