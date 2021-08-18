# import sys
# N , K = map(int, sys.stdin.readline().split())

N, K = map(int, input().split())
queue = list(range(1, N+1))
qidx = K-1

josephus = []
while queue:
    if qidx < len(queue):
        josephus.append(str(queue.pop(qidx)))
        qidx += K-1
    elif qidx >= len(queue):
        while qidx >= len(queue):
            qidx -= len(queue)
        josephus.append(str(queue.pop(qidx)))
        qidx += K-1
    if len(queue) == 1:
        josephus.append(str(queue.pop(0)))
print('<', ', '.join(josephus), '>', sep='')
