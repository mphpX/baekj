import sys
n=int(sys.stdin.readline())
s=0
c=1
while(s<=n):
    s=(c+2)*(c+1)//2
    c+=1
print(c-1)