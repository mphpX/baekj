import sys
import heapq
heap=[]
n=int(sys.stdin.readline())
for i in range(n):
    a=int(sys.stdin.readline())
    if(a!=0):
        heapq.heappush(heap,-a)
    else:
        if(len(heap)==0):
            print(0)
        else:
            x=heapq.heappop(heap)
            print(-x)