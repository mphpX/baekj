from collections import deque
a,b=map(int,input().split())
q=deque([0])
ct=0
while(q):
    cur=q.popleft()
    left=cur*10+4
    right=cur*10+7
    if(left<=b):
        q.append(left)
        if(a<=left):
            ct+=1
    if(right<=b):
        q.append(right)
        if(a<=right):
            ct+=1
print(ct)