N, K = map(int, input().split())
coin = []
for i in range(N):
    coin.append(int(input()))

cnt = 0
for c in coin[::-1]:
    if K >= c:
        cnt += K // c
        K = K % c

print(cnt)