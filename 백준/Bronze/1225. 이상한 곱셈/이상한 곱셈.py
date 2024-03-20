import sys
a,b=sys.stdin.readline().split()
a,b=list(map(int,a)),list(map(int,b))
print(sum(a)*sum(b))