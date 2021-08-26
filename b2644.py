import sys
sys.stdin = open('input.txt')

def bfs():
    relationship = [0] * (n+1)
    q = [s]
    relationship[s] = 1

    while q:
        now = q.pop(0)

        for i in range(1, n+1):
            if not relationship[i] and family[now][i]:
                q.append(i)
                relationship[i] = relationship[now] + 1

                if i == g:
                    return (relationship[i] - 1)
    return -1



n = int(input())
s, g = map(int, input().split())
m = int(input())
family = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    family[x][y] = family[y][x] = 1

print(bfs())