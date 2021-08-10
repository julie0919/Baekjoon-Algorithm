import sys

book = int(input())
book_list =[int(sys.stdin.readline())]

cnt = 0
max_book = book_list[0]

for i in range(1, book):
    book_list.append(int(sys.stdin.readline()))

for book_num in range(1, book):
    if book_list[book_num] > max_book:
        if max_book + 1 != book_list[book_num]:
            cnt += 1
        max_book = book_list[book_num]
    else:
        cnt += 1

print(cnt)