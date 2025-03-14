import math
n=int(input())
l=list(map(int,input().split()))
t,p=map(int,input().split())
ct=0
for i in l:
    ct+=math.ceil(i / t)
print(ct)
print(n//p,n-n//p*p)