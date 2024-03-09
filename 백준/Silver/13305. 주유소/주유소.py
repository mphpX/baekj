import sys
n=int(input())
a=list(map(int,sys.stdin.readline().split()))
b=list(map(int,sys.stdin.readline().split()))
ct=a[0]*b[0]
s=b[0]
for i in range(1,n-1):
    if(s>b[i]):
        s=b[i]
    ct+=s*a[i]
print(ct)