import sys
n=int(input())
num=[1,1,1,1,1,1,1,1,1,1]

for i in range(1,n):
    arr=[]
    for i in range(10):
        x=0
        for j in range(i+1):
            x+=num[j]
        arr.append(x%10007)
    num=arr
print(sum(num)%10007)