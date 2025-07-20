def solution(names):
    answer = []
    l=len(names)
    cur=0
    while(cur<l):
        answer.append(names[cur])
        cur+=5
    return answer