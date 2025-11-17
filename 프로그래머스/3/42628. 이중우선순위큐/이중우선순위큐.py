import heapq
def solution(operations):
    min_heap= []
    max_heap= []
    d= dict()
    for op in operations:
        o,p= op.split()
        p = int(p)
        if(o=='I'):
            if(p in d): 
                d[p]+= 1
            else:
                d[p]= 1
            heapq.heappush(min_heap,p)
            heapq.heappush(max_heap,-p)
        else:
            if(p == 1):
                while(max_heap and d.get(-max_heap[0], 0) == 0):
                    heapq.heappop(max_heap)
                if(max_heap):
                    idx=-heapq.heappop(max_heap)
                    d[idx]-=1
                    
            else:
                while(min_heap and d.get(min_heap[0],0)== 0):
                    heapq.heappop(min_heap)
                if(min_heap):
                    idx= heapq.heappop(min_heap)
                    d[idx]-= 1
    maxx,minn= 0,0
    while(max_heap and d.get(-max_heap[0], 0) == 0):
        heapq.heappop(max_heap)
    if(max_heap):
        maxx=-heapq.heappop(max_heap)
    while(min_heap and d.get(min_heap[0],0)== 0):
        heapq.heappop(min_heap)
    if(min_heap):
        minn= heapq.heappop(min_heap)
    return [maxx,minn]