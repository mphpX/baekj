T = int(input())
def back_track(n,menu,limit, s, cur_k, cur_p, ans):
    if(limit<cur_k):
        return
    ans.add(cur_p)
    for i in range(s, n):
        next_k = cur_k+ menu[i][1]
        next_p = cur_p+ menu[i][0]
        if(next_k <= limit):
            back_track(n,menu,limit, i+1, next_k, next_p, ans)
    
for test_case in range(1, T + 1):
    n, l = map(int,input().split())
    menu=[]
    visited=[0 for _ in range(n)]
    ans= set()
    for i in range(n):
        t,k= map(int,input().split())
        menu.append((t,k))
    back_track(n,menu,l, 0, 0, 0, ans)
    print('#',test_case,' ',max(ans),sep='')