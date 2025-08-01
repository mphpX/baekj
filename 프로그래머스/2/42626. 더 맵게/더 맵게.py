import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer=0
    while(True):
        a=heapq.heappop(scoville)
        if(a>=K):
            break
        if(len(scoville)==0):
            answer=-1
            break
        b=heapq.heappop(scoville)
        heapq.heappush(scoville,a+b*2)
        answer+=1
    return answer