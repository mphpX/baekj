import sys
from collections import deque
n=int(sys.stdin.readline())
num=[0 for i in range(21)]
for i in range(n):
    l=list(sys.stdin.readline().split())
    if(len(l)==2):
        x=int(l[1])
    if(l[0]=='add'):
        num[x]+=1
    elif(l[0]=='remove'):
        if(num[x]>0):
            num[x]=0
    elif(l[0]=='check'):
        if(num[x]>0):
            print(1)
        else:
            print(0)
    elif(l[0]=='toggle'):
        if(num[x]>0):
            num[x]=0
        else:
            num[x]+=1
    elif(l[0]=='all'):
        for i in range(1,21):
            num[i]=1
    elif(l[0]=='empty'):
        for i in range(1,21):
            num[i]=0