num = int(input())

n = 1
while (n * (n + 1)) / 2 <= num:
    n += 1
print(n - 1)