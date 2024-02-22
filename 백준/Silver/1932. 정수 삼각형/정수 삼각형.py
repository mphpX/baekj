import sys
n=int(input())
t=[]
result=[]
for i in range(n):
    l=list(map(int,sys.stdin.readline().split()))
    t.append(l)
result.append([t[0][0]])
if(n>=2):
    result.append([t[0][0]+t[1][0],t[0][0]+t[1][1]])
for i in range(2,n):
    a=[]
    for j in range(i+1):
        if(j==0):
            a.append(result[i-1][j]+t[i][j])
        elif(j<i):
            a.append(max(result[i-1][j-1],result[i-1][j])+t[i][j])
        else:
            a.append(result[i-1][j-1]+t[i][j])
    result.append(a)
print(max(result[n-1]))