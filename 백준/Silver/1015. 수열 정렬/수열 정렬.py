n=int(input())
a=list(map(int,input().split()))
p=[0 for i in range(n)]
nums=[]
for i in range(n):
    nums.append([a[i],i])
nums.sort()

for i in range(n):
    p[nums[i][1]]=i
for i in p:
    print(i,end=' ')