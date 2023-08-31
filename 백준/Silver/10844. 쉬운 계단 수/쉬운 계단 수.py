import sys
arr=[[0],[0,1,1,1,1,1,1,1,1,1]]
n=int(input())
s=9
for i in range(2,n+1):
    num=[]
    for j in range(10):
        if(j<1):
            num.append(arr[i-1][j+1]%1000000000)
        elif(j<9):
            num.append((arr[i-1][j-1]+arr[i-1][j+1])%1000000000)
        else:
            num.append(arr[i-1][8]%1000000000)
    arr.append(num)
    s=sum(num)%1000000000
print(s)