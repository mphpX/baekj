num=[]
for i in range(9):
    num.append(int(input()))
num.sort()
target=sum(num)-100
ans=[0,0]
for i in range(9):
    for j in range(i+1,9):
        if(num[i]+num[j]==target):
            ans[0]=i
            ans[1]=j
for i in range(9):
    if(i!=ans[0] and i!=ans[1]):
        print(num[i])