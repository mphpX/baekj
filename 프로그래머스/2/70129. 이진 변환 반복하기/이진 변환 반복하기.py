def solution(s):
    one=0
    st=s
    ct=0
    zero=0
    while(one!=1):
        one=0
        for i in st:
            if(i=='1'):
                one+=1
        zero+=len(st)-one
        st=bin(one)[2:]
        ct+=1
    
    answer = [ct,zero]
    return answer