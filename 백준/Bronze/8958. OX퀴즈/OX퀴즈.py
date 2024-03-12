import sys
n=int(input())
for i in range(n):
    l=list(sys.stdin.readline())
    result=0
    ct=0
    for i in l:
        if(i=='O'):
            ct+=1
        else:
            result+=ct*(ct+1)//2
            ct=0
    print(result)