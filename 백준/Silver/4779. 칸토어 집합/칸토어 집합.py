import sys
def recur(x):
    if(x==0):
        return '-'
    prev=recur(x-1)
    space=' '*(3**(x-1))
    return prev + space + prev
while(True):
    try:
        n=int(sys.stdin.readline().strip())
        result=recur(n)
        print(result)
    except:
        break