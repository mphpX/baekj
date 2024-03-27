import sys
import heapq
que=[]
t=int(sys.stdin.readline())
for i in range(t):
    n=int(sys.stdin.readline())
    if(n!=0):
        heapq.heappush(que,n)
    else:
        if(len(que)==0):
            print(0)
        else:
            print(heapq.heappop(que))
