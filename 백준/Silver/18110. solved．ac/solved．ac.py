import sys
import math
n=int(sys.stdin.readline())
l=[]
for i in range(n):
    a=int(sys.stdin.readline())
    l.append(a)
if(n==0):
    print(0)
else:
    l.sort()
    x=math.floor(n*15/100+0.5)
    print(math.floor(sum(l[x:n-x])/(n-2*x)+0.5))