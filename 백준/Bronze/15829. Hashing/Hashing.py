import sys
n=int(sys.stdin.readline())
l=list(sys.stdin.readline().strip())
ct=0
for i in range(n):
    ct+=(ord(l[i])-96)*(31**i)
print(ct%1234567891)