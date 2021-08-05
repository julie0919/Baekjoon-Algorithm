num = int(input())

cnt = 0
while True:
    if not bool(num % 5):
        cnt += num // 5
        print(cnt)
        break
    num -= 3
    cnt += 1

    if num < 0:
        print(-1)
        break