def solution(s):
    answer = ''
    need = 1
    for i in s:
        if(i==' '):
            answer+= ' '
            need = 1
        elif(need==1):
            answer+= i.upper()
            need = 0
        else:
            answer+=i.lower()
    return answer