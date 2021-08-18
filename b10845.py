import sys

N = int(sys.stdin.readline())

queue = []

for i in range(N):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push":
        queue.insert(0, cmd[1])
        ##print(queue)

    elif cmd[0] == "pop":
        if len(queue) != 0: print(queue.pop())
        else: print(-1)

    elif cmd[0] == "size":
        print(len(queue))

    elif cmd[0] == "empty":
        if len(queue) == 0: print(1)
        else : print(0)

    elif cmd[0] == "front":
        if len(queue) == 0: print(-1)
        else: print(queue[len(queue) -1])

    elif cmd[0] == "back":
        if len(queue) == 0: print(-1)
        else: print(queue[0])

# 직접 구현
# class Queue():
#     def __init__(self):
#         self.queue = []

#     # Push
#     def push(self, data):
#         self.queue.append(data)

#     # Pop
#     def pop(self):
#         pop_object = None
#         if self.empty():
#             print(-1)
#         else:
#             pop_object = self.queue[0]
#             self.queue = self.queue[1:]
#         return pop_object

#     # Size
#     def size(self):
#         return len(self.queue)

#     # Empty
#     def empty(self):
#         is_empty = 0
#         if len(self.queue) == 0:
#             is_empty = 1
#         return is_empty

#     # Front
#     def front(self):
#         front_object = None
#         if self.empty():
#             print(-1)
#         else:
#             front_object = self.queue[0]
#         return front_object

#     # Back
#     def back(self):
#         back_object = None
#         if self.empty():
#             print(-1)
#         else:
#             back_object = self.queue[-1]
#         return back_object

# N = int(sys.stdin.readline())
# for _ in range(N):
#     cmd = sys.stdin.readline().split()

# q = Queue()
# if cmd[0] == "push":
#     q.push(cmd[1])
# elif cmd[0] == "front":
#     q.front()
# elif cmd[0] == "back":
#     q.back()
# elif cmd[0] == "size":
#     q.size()
# elif cmd[0] == "empty":
#     q.empty()
# elif cmd[0] == "pop":
#     q.pop()