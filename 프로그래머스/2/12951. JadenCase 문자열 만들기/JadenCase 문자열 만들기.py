def solution(s):
    result = []
    need = 1
    for i in s:
        if i == ' ':
            result.append(' ')
            need = 1
        elif need == 1:
            result.append(i.upper())
            need = 0
        else:
            result.append(i.lower())
    return ''.join(result)