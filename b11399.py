n = int(input())

num_list = sorted(list(map(int, input().split())))

sum_list = []
for i in range(1, len(num_list) + 1):
    sum_list.append(sum(num_list[:i]))

print(sum(sum_list))

