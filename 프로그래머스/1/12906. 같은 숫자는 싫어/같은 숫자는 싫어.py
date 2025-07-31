def solution(arr):
    answer = [arr[0]]
    cur=arr[0]
    for i in arr:
        if(cur!=i):
            answer.append(i)
            cur=i
    return answer