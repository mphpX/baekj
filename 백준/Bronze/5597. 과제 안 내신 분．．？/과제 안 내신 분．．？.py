

num_list= []
for i in range(28):
    num_list.append(int(input()))

for k in range(1,31):
    if k not in num_list:
        print(k)