import sys

N = int(sys.stdin.readline())

for tc in range(1, N+1):
    word = sys.stdin.readline().split() 

    print('Case #{}:'.format(tc), end=' ')
    while word:
        print(word.pop(), end=' ')
    print()
