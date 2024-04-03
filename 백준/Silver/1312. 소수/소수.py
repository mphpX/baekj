import sys
a,b,c=map(int,sys.stdin.readline().split())
for i in range(c):
    a=(a%b)*10
    x=a//b
print(x)