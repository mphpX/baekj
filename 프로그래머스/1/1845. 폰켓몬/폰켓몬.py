def solution(nums):
    d=dict()
    for i in nums:
        if(i in d):
            d[i]+=1
        else:
            d[i]=1
    nct=len(nums)//2
    dct=len(d)
    if(dct<nct):
        answer=dct
    else:
        answer=nct
    return answer