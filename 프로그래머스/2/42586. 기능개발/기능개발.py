def solution(progresses, speeds):
    cur=0
    n=len(speeds)
    answer=[]
    while(cur< n):
        time= ((100-progresses[cur])+speeds[cur]-1)//speeds[cur]
        ct=0
        for i in range(cur,n):
            progresses[i]+=time* speeds[i]
        for i in range(cur,n):
            if(progresses[i]>99):
                ct+=1
                cur=i+1
            else:
                break
        answer.append(ct)
        
    return answer