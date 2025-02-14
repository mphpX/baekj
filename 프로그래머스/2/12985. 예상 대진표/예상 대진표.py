def solution(n,a,b):
    x,y=a-1,b-1
    ct=0
    while(x!=y):
        x//=2
        y//=2
        ct+=1
    return ct