import sys
n=int(sys.stdin.readline())
f=int(sys.stdin.readline())
n=n//100*100
while(True):
    if(n%f==0):
        a=n%100
        if(a<10):
            print(0,a,sep='')
        else:
            print(a)
        break
    n+=1