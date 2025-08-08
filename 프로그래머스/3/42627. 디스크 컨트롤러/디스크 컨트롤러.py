import heapq
def solution(jobs):
    answer = 0
    n= len(jobs)
    wait= []
    heapq.heapify(wait)
    timestamp= dict()
    for idx in range(n):
        start, time = jobs[idx][0], jobs[idx][1]
        if(start not in timestamp):
            timestamp[start]= []
        timestamp[start].append((time, idx))
    cur= 0
    done= 0
    post_cur=0
    while(done< n):
        for t in range(post_cur,cur+1):
            if t in timestamp:
                for time,idx in timestamp[t]:
                    heapq.heappush(wait,(time,t,idx))
        if(wait):
            i_time, i_start, i_idx= heapq.heappop(wait)
            post_cur= cur+1
            cur+=i_time
            done+=1
            answer+= cur- i_start
        else:
            post_cur= cur+1
            cur+=1
    return answer//n