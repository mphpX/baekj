import sys
from collections import deque  
n=int(sys.stdin.readline())
ans=deque()
l=deque()
ch=[]
for i in range(n):
    a=int(sys.stdin.readline())
    ans.append(a)
ct=1
while(ct<=ans[0]):
    l.append(ct)
    ch.append('+')
    ct+=1
ans.popleft()
l.pop()
ch.append('-')
while(len(ans)>0):
    if(ct==ans[0]):
        ans.popleft()
        ch.append('+')
        ch.append('-')
        ct+=1
    elif(ct<ans[0]):
        while(ct!=ans[0]):
            l.append(ct)
            ct+=1
            ch.append('+')
        ans.popleft()
        ch.append('+')
        ch.append('-')
        ct+=1
    else:
        if(ans[0]==l[len(l)-1]):
            ch.append('-')
            ans.popleft()
            l.pop()
        else:
            ct=-1
            break
if(ct==-1):
    print("NO")
else:
    for i in ch:
        print(i)