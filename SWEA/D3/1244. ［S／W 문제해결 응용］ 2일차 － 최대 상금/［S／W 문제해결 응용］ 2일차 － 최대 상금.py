T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

def back_track(l, r, num_set, visited):
    if(r==0):
        num_set.add(int("".join(map(str, l))))
        return
    state= (tuple(l), r)
    if(state in visited):
        return
    visited.add(state)
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            l[i],l[j]= l[j],l[i]
            back_track(l, r-1, num_set,visited)
            l[i],l[j]= l[j],l[i]
            
for test_case in range(1, T + 1):
    n, r = map(int,input().split())
    nums=list(map(int, str(n)))
    num_set=set()
    visited= set()
    back_track(nums, r, num_set, visited)
    print('#',test_case,' ', max(num_set), sep='')