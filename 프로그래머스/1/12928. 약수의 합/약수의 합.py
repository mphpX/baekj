def solution(n):
    if(n==0):
        return 0
    ans=set()
    for i in range(1,n//2+2):
        if(n%i==0):
            ans.add(i)
            ans.add(n//i)
    return sum(ans)