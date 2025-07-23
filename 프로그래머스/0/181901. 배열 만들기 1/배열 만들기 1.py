def solution(n, k):
    answer = []
    cur=k
    while(cur<=n):
        answer.append(cur)
        cur+=k
    return answer