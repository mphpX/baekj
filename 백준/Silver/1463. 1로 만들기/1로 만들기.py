import sys
arr=[0,0,1,1]
n=int(input())
for i in range(4,n+1):
    if(i%3==0 and i%2==0):arr.append(min(arr[i//3],arr[i//2],arr[i-1])+1)
    elif(i%3==0):arr.append(min(arr[i//3],arr[i-1])+1)
    elif(i%2==0):arr.append(min(arr[i//2],arr[i-1])+1)
    else:arr.append(arr[i-1]+1)
print(arr[n])