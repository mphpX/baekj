import sys
input=sys.stdin.readline
case=int(input())
for i in range(case):
    l=list(map(int,input().split()))
    avg=sum(l[1:l[0]+1])/l[0]
    ct=0
    for i in range(1,l[0]+1):
        if(l[i]>avg):
            ct+=1
    print("{:.3f}%".format(ct/l[0]*100))