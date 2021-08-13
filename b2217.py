N = int(input())
rope = []
for _ in range(N):
    rope.append(int(input()))

rope.sort(reverse=True)

maxV = rope[0]
for i in range(N):
    if maxV < rope[i] * (i+1):
        maxV = rope[i] * (i+1)
print(maxV)
