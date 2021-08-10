city = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))

min_price = price[0]
total = 0

for i in range(city - 1):
    if min_price > price[i]:
        min_price = price[i]
    total += (min_price * dist[i])

print(total)