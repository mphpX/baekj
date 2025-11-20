#import sys
#sys.stdin = open("input.txt", "r")
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    # 1 2 3 1 7 1 2 3 10
    n= int(input())
    price= list(map(int,input().split()))
    answer= 0
    cur= price.pop()
    while(price):
        next= price.pop()
        if(next<cur):
            answer+=cur-next
        else:
            cur= next
    print('#',test_case,' ',answer, sep='')
    # ///////////////////////////////////////////////////////////////////////////////////
