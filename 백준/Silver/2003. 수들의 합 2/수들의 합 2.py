import sys
input= sys.stdin.readline
n,m=map(int,input().split())
arr=list(map(int,input().split()))
sm=[0 for _ in range(n+1)]
for i in range(1,n+1):
    sm[i]=arr[i-1]
for i in range(1,n+1):
    sm[i]+=sm[i-1]
ct=0
for i in range(n+1):
    for j in range(i+1,n+1):
        if(sm[j]-sm[i]==m):
            ct+=1
            break
        elif(sm[j]-sm[i]>m):
            break
print(ct)