def solution(triangle):
    before= [triangle[0][0]]
    after= []
    for i in range(1,len(triangle)): # i층
        for j in range(i+1): # column 0~i
            if(j==0):
                after.append(before[j]+triangle[i][j])
            elif(j==i):
                after.append(before[j-1]+triangle[i][j])
            else:
                after.append(max(before[j-1],before[j])+triangle[i][j])
        before=after
        after=[]
    return max(before)