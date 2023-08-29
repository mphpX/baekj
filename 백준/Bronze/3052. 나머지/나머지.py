import sys
arr=[]
for i in range(42):
    arr.append(0)
for i in range(10):
    x=int(input())
    arr[x%42]+=1
ct=0
for i in range(42):
    if(arr[i]>0):ct+=1
print(ct)