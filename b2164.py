# 규칙성
N = int(input())
cnt = 0
test = N
while test > 1:
    test = test // 2
    cnt += 1
result = 0
if N == 1:
    result = 1
elif N == 2 ** cnt:
    result = N
else:
    result = N%(2**cnt) * 2
print(result)


# 시간초과
# import sys

# card = list(range(1, int(input())+1))
# while len(card) > 1:
#     card.pop(0)
#     card.append(card.pop(0))
# print(*card)

# 런타임에러
# def stk(c_list):
#     if len(c_list) >1:
#         c_list.pop(0)
#         c_list.append(c_list.pop(0))
#         stk(c_list)
#     else:
#         print(*c_list)

# card = list(range(1, int(input()+1)))
# stk(card)
