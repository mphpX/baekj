def solution(numbers, target):
    answer = [0]
    def back_track(ct, s):
        if(ct==len(numbers)):
            if(s== target):
                answer[0]+=1
            return
        back_track(ct+1,s+numbers[ct])
        back_track(ct+1,s-numbers[ct])
    back_track(0,0)
    return answer[0]