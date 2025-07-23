def solution(t, p):
    lt=len(t)
    lp=len(p)
    num=[]
    for i in range(lt-lp+1):
        num.append(int(t[i:i+lp]))
    answer=0
    for i in num:
        if(int(p)>=i):
            answer+=1
    return answer