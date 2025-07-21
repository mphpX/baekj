def solution(n, w, num):
    num-=1
    remainder=[0 for _ in range(2*w)]
    for i in range(n):
        remainder[i%(2*w)]+=1
    num_idx=num%(2*w)
    print(remainder)
    answer=remainder[num_idx]-num//w+remainder[2*w-1-num_idx]
    return answer