import sys
n=int(input())
num=[[],[1,0,0],[0,1,0],[1,1,1]]

for i in range(4,100001):
    x=[]
    for j in range(1,4):
        s=0
        for k in range(3):
            if(j!=k+1):
                s+=num[i-j][k]
        x.append(s%1000000009)
    num.append(x)
for i in range(n):
    m=int(input())
    print(sum(num[m])%1000000009)