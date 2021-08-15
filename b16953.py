A, B = map(int, input().split())

cnt = 0

while True:
    if B % 2:
        B = (B -1) / 10
        cnt += 1
    else:
        B = B / 2
        cnt += 1
    
    if A == B:
        print(cnt + 1)
        break
    elif A > B:
        print(-1)
        break