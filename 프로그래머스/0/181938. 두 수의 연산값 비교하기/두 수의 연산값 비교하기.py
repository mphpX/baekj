def solution(a, b):
    ct=0
    while(10**ct<b):
        ct+=1
    return max(2*a*b, 10**ct*a+b)