blank= []
for i in range(9):
    blank.append(int(input()))

# max_num = max(blank)
# print(max_num)
idx=0
for k in range(len(blank)):
    if blank[k] >blank[idx]:
        idx= k
print(blank[idx])
print(idx+1)