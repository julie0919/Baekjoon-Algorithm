T = int(input())
for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))
    disc = []
    origin = []
    p = 0

    while price:
        if p == N*2:
            origin.append(price.pop(0))
        else:
            find = price.pop(0)

            for i in range(N*2 - p):
                if price[i]*0.75 == find:
                    origin.append(price.pop(i))
                    disc.append(find)
                    break
                else:
                    origin.append(find)

        p += 1

    print('Case #{}:'.format(tc), end=' ')
    for d in disc:
        print(d, end=' ')
    print()

