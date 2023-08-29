import sys
arr=[0,0,1,0]
n=int(input())
for i in range(4,n+1):
    if(arr[i-1]==1 or arr[i-3]==1):
        arr.append(0)
    else:arr.append(1)
if(arr[n]==0):print("SK")
else:print("CY")