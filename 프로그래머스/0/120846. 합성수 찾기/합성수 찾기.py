def solution(n):
    ss=[2,3]
    for i in range(4,11):
        ct=0
        for j in range(2,i):
            if(i%j==0):
                ct=1
                break
        if(ct==0):
            ss.append(i)
    ans=[0 for i in range(n+1)]
    print(ss)
    for i in ss:
        test=i
        j=2
        while(test*j<=n):
            ans[test*j]=1
            j+=1
    return sum(ans)