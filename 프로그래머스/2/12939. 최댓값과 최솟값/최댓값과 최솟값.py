def solution(s):
    x=list(map(int, s.split()))
    return str(min(x))+" " + str(max(x))