# N = int(input())
# p1 = list(map(int, input().split()))
N = 3
p1 = [2, 3, 1]
p2 = []
p3 = []
sort_p1 = sorted(p1)

cnt = 0
result = []

while True:
    if sort_p1[-1] in p1:
        if p1[-1] == sort_p1[-1]:
            p3.append(p1.pop())
            cnt += 1
            result.append([1, 3])
            sort_p1.pop()
        else:
            p2.append(p1.pop())
            cnt += 1
            result.append([1, 2])

    elif sort_p1[-1] in p2:
        if p2[-1] == sort_p1[-1]:
            p3.append(p2.pop())
            cnt += 1
            result.append([2, 3])
            sort_p1.pop()
        else:
            p1.append(p2.pop())
            cnt += 1
            result.append([2, 1])
    
    if not p1 and not p2:
        break

print(cnt)
for row in result:
    print(*row)



