def solution(citations):
    citations.sort()
    n=len(citations)
    if(n==0): return 0
    answer=0
    j=0
    for i in range(n+1):
        while(j<n and citations[j]<i):
            j+=1
        cnt= n-j
        if(cnt>= i):
            answer=i
    return answer