import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    log = sorted(list(map(int, input().split())))

    new = []
    if N % 2:
        for num in log[0:N:2]:
            new.append(num)
        for num in log[N-2:0:-2]:
            new.append(num)
    else:
        for num in log[0:N:2]:
            new.append(num)
        for num in log[N-1:0:-2]:
            new.append(num)
    
    diff = []
    diff.append(abs(new[0] - new[-1]))
    for i in range(N-1):
        diff.append(abs(new[i] - new[i+1]))
    print(max(diff))

    