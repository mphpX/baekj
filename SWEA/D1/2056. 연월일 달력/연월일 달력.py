T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
ex=[31,28,31,30,31,30,31,31,30,31,30,31]
for test_case in range(1, T + 1):
    ymd= input().strip()
    m=int(ymd[4:6])
    d=0
    if(0< m <13):
        d=int(ymd[6:])
    if(0< d<= ex[m-1]):
        print('#', test_case, ' ',''.join(ymd[:4]+'/'+ ymd[4:6]+'/'+ ymd[6:]), sep='')
    else:
        print('#', test_case, ' ',-1,sep='')
        
    
    