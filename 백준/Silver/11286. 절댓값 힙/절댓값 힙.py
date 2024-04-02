import sys, heapq
h=[]
n = int(sys.stdin.readline())
for i in range(n):
	x = int(sys.stdin.readline())
	if x!=0:
		heapq.heappush(h, (abs(x), x))
	else:
		if h:
			print(heapq.heappop(h)[1])
		else:
			print(0)