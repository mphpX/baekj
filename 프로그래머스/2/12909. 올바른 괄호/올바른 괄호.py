def solution(s):
    l=[]
    for i in s:
        if(i=='('):
            l.append(i)
        else:
            if(len(l)==0):
                return False
            else:
                l.pop()
    if(len(l)==0):
        return True
    else:
        return False