n = int(input())
sam= [0, 3, 6, 9]
graph=[0 for _ in range(1001)]
cur= 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            cur=(i%3==0 and i!=0) + (j%3==0 and j !=0)+ (k%3==0 and k!=0)
            graph[i*100+ j*10+ k*1]= cur
for i in range(1, n + 1):
    print( ('-' * graph[i] if graph[i] else i), end=' ')