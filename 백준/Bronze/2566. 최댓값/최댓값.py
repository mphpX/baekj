import sys
arr=[]
m=-1
for i in range(9):
    num=list(map(int,input().split()))
    arr.append(num)
    if(max(num)>m):
        m=max(num)
        mi=i
        mj=num.index(m)
print("%d\n%d %d"%(m,mi+1,mj+1))