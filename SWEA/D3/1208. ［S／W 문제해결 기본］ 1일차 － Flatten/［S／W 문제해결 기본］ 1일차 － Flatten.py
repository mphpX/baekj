for case in range(1, 11):
    n=int(input())
    graph=[0 for _ in range(101)]
    boxes= list(map(int,input().split()))
    for i in boxes:
        graph[i]+=1
    high, low= 100, 1
    while(n):
        if(high<=low):
            break
        if(graph[high]==0):
            high-=1
        elif(graph[low]==0):
            low+=1
        else:
            graph[high]-=1
            graph[high-1]+=1
            graph[low]-=1
            graph[low+1]+=1
            n-=1
    low,high=0,0
    for i in range(1, 101):
        if(graph[i]>0):
            low=i
            break
    for i in range(100,-1,-1):
        if(graph[i]>0):
            high=i
            break
    print('#',case,' ',high-low, sep='')