def solution(s):
    alpha=[-1 for _ in range(26)]
    answer = []
    for i in range(len(s)):
        idx=ord(s[i])-97
        if(alpha[idx] == -1):
            answer.append(-1)
            alpha[idx] = i
        else:
            answer.append(i-alpha[idx]) 
            alpha[idx]=i
    return answer