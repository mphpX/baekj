import sys
arr=[-1,-1,-1,1,-1,1]
n=int(input())
for i in range(6,n+1):
    if(arr[i-3]>0 and arr[i-5]>0):arr.append(1+min(arr[i-3],arr[i-5]))
    elif(arr[i-3]>0):arr.append(arr[i-3]+1)
    elif(arr[i-5]>0):arr.append(arr[i-5]+1)
    else:arr.append(-1)
print(arr[n])