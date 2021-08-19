import sys

K = int(sys.stdin.readline())
num_list = []
for _ in range(K):
    num = int(sys.stdin.readline())

    if num:
        num_list.append(num)
    else:
        num_list.pop()
print(sum(num_list))