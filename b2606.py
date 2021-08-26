def dfs():
    visit = [0]*(computer+1)
    stk = [1]
    visit[1] = 1

    while stk:
        now = stk.pop()
        for i in range(1, computer+1):
            if not visit[i] and network[now][i]:
                visit[i] = 1
                stk.append(i)
    return visit



computer = int(input())
n = int(input())
line = [list(map(int, input().split())) for _ in range(n)]
network = [[0]*(computer+1) for _ in range(computer+1)]

for l in line:
    network[l[0]][l[1]] = network[l[1]][l[0]] = 1

print(sum(dfs()) - 1)