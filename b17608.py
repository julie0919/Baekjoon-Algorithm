import sys

N = int(sys.stdin.readline())
stick = []
for _ in range(N):
    stick.append(int(sys.stdin.readline()))

cnt = 1
max_stick = stick[-1]
for i in range(N-2, -1, -1):
    if stick[i] > max_stick:
        cnt += 1
        max_stick = stick[i]
print(cnt)