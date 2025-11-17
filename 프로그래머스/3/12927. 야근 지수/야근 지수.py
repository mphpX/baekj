import heapq
def solution(n, works):
    total= sum(works)
    heap= []
    for work in works:
        heapq.heappush(heap, -work)
    while(n and heap):
        if(total==0):
            break
        target= heapq.heappop(heap)
        if(target<0):
            target+=1
            heapq.heappush(heap,target)
            n-=1
            total-=1
    answer= 0
    for h in heap:
        answer+=h*h
    return answer