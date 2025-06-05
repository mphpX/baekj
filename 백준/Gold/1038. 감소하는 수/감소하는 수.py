from collections import deque
n=int(input())
basic=deque([1,2,3,4,5,6,7,8,9])
ans=[0,1,2,3,4,5,6,7,8,9]
ct=9
while(basic):
    if(ct>=n):
        break
    cur=basic.popleft()
    for i in range(cur%10):
        ans.append(cur*10+i)
        basic.append(cur*10+i)
        ct+=1
if(ct>= n):
    print(ans[n])
else:
    print(-1)