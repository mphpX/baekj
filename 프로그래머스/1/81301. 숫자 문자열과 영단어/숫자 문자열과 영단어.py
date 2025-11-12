def solution(s):
    d= dict()
    st= ['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(10):
        d[st[i]] = i
    i=0
    answer = 0
    while(i<len(s)):
        if(s[i].isdigit()):
            answer= answer+int(s[i])
        else:
            for j in range(1,5):
                target = s[i:i+j+1]
                if(target in d):
                    answer= answer + d[target]
                    i = i+j
                    break
        i+=1
        answer*=10
    return answer//10