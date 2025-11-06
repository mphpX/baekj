def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    i=0
    j=len(B)-1
    while(i<len(A) and j>=0):
        answer+=A[i]*B[j]
        i+=1
        j-=1

    return answer