def solution(answers):
    answer = [0,0,0]
    second= [2,1,2,3,2,4,2,5]
    third= [3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        if((i+1)%5== answers[i]%5):
            answer[0]+=1
        if(answers[i]== second[i%8]):
            answer[1]+=1
        if(answers[i]== third[i%10]):
            answer[2]+=1
    m= max(answer)
    ans=[]
    for i in range(3):
        if(answer[i]==m):
            ans.append(i+1)
    return ans