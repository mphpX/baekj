import sys
from sys import stdin
n=int(input())
for i in range(n):
    m,o=map(int,input().split(','))
    print(m+o)