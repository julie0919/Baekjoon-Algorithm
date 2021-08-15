def first_pal(word, left, right):
    while left < right:
        if (word[left] == word[right]):
            left += 1
            right -= 1
        else:
            del_left = second_pal(word, left+1, right)
            del_right = second_pal(word, left, right-1)
            if (del_left or del_right):
                return 1
            else:
                return 2
    return 0

def second_pal(word, left, right):
    while left < right:
        if (word[left] == word[right]):
            left += 1
            right -= 1
        else:
            return False
    return True



T = int(input())
for tc in range(1, T+1):
    word = input()
    left = 0
    right = len(word) - 1
    print(first_pal(word, left, right))


# 시간초과
# def ispal(testword):
#     for w in range(len(testword)):
#         ispal = testword[0:w] + testword[w+1:]
#         if ispal == ispal[::-1]:
#             return 1
#     return 2


# T = int(input())
# for tc in range(1, T+1):
#     word = input()

#     if word == word[::-1]:
#         print(0)

#     else:
#         print(ispal(word))