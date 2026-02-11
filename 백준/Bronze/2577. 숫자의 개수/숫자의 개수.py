num_list=[]
for i in range(3):
    num_list.append(int(input()))

result=1
for k in num_list:
    result *= k
    re_result=str(result)

blank = [0] * 10
for i in range(10):
    if str(i) in re_result:
        blank[i]+=re_result.count(str(i))
        # blank[i] += 1
print(*blank, sep='\n')