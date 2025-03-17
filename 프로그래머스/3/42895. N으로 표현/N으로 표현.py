def solution(N, number):
    dp=[set() for i in range(10)]
    ct=N
    for i in range(1,10):
        dp[i].add(ct)
        ct=ct*10+N
    for i in range(1, 10):
        for j in range(1,i):
            for op1 in dp[j]:
                for op2 in dp[i-j]:
                    dp[i].add(op1+op2)
                    dp[i].add(op1-op2)
                    dp[i].add(op1*op2)
                    if(op2!=0):
                        dp[i].add(op1//op2)
        if number in dp[i]:
            return i
    return -1