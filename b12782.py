def cnt1(strb):
    cnt = 0
    for b in strb:
        if b == '1':
            cnt += 1
    return cnt


T = int(input())

for tc in range(1, T+1):
    N, M = input().split()
    change1 = 0

    if cnt1(N) == cnt1(M):
        pass
    else:
        change1 += abs(cnt1(N) - cnt1(M))

    diff = 0
    for i in range(len(N)):
        if N[i] != M[i]:
            diff += 1
    print(change1 + (diff - change1)//2)
