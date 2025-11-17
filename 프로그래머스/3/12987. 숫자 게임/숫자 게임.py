def solution(A, B):
    B.sort()
    A.sort()
    i,j=0,0
    answer= 0
    while(i< len(A) and j< len(B)):
        if(A[i]>=B[j]):
            j+=1
        else:
            answer+=1
            i+=1
            j+=1
    return answer