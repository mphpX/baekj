def solution(participant, completion):
    d=dict()
    for i in participant:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    for i in completion:
        d[i]-=1
    for i in d:
        if(d[i]==1):
            return i