def validate(ps):
    stk1 = []
    for p in ps:
        if p == ')' and stk1:
            if stk1[-1] == '(':
                stk1.pop()
            else:
                stk1.append(p)
        elif p == ']' and stk1:
            if stk1[-1] == '[':
                stk1.pop()
            else:
                stk1.append(p)
        else:
            stk1.append(p)
    if stk1:
        return False
    else:
        return True


def calc(ps):
    stk = []
    for p in ps:
        if p == ')':
            if stk[-1] == '(':
                stk.pop()
                stk.append(2)
            else:
                temp = 0
                while stk:
                    if stk[-1] == '(':
                        stk.pop()
                        stk.append(temp * 2)
                        break
                    else:
                        temp += stk.pop()
        elif p == ']':
            if stk[-1] == '[':
                stk.pop()
                stk.append(3)
            else:
                temp = 0
                while stk:
                    if stk[-1] == '[':
                        stk.pop()
                        stk.append(temp * 3)
                        break
                    else:
                        temp += stk.pop()
        else:
            stk.append(p)
    return sum(stk)
                

par = list(input())
if not validate(par):
    print(0)
else:
    print(calc(par))


# 런타임 에러 (ValueError)
# while par:
#     if len(par) == 1:
#         stk.append(par.pop(0))
#     else:
#         if par[0] == '(' and par[1] == ')':
#             stk.append('2')
#             par.pop(0)
#             par.pop(0)
#         elif par[0] == '[' and par[1] == ']':
#             stk.append('3')
#             par.pop(0)
#             par.pop(0)
#         else:
#             stk.append(par.pop(0))

# i = 0
# while i < len(stk):
#     if stk[i] == ')':
#         temp = 0
#         while len(calc) != 0:
#             if calc[-1].isdigit():
#                 temp += int(calc.pop())
#             else:
#                 calc.pop()
#                 calc.append(str(temp * 2))
#                 i += 1
#                 break

#     elif stk[i] == ']':
#         temp = 0
#         while len(calc) != 0:
#             if calc[-1].isdigit():
#                 temp += int(calc.pop())
#             else:
#                 calc.pop()
#                 calc.append(str(temp * 3))
#                 i += 1
#                 break

#     else:
#         calc.append(stk[i])
#         i += 1

# calc = list(map(int, calc))

# result = 0
# for num in calc:
#     if num:
#         result += num
#     else:
#         result = 0
#         break
# print(result)



