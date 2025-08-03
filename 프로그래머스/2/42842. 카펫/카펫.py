def solution(brown, yellow):
    for i in range(1,int(yellow**(1/2))+1):
        if(yellow%i==0):
            a= i
            b= yellow//i
            if((a+2)*2+b*2== brown):
                return [b+2,a+2]
    return