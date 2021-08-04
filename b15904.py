word = input()
alp = ['U', 'C', 'P', 'C']
i = 0

for a in alp:
    if a in word:
        i += 1
        word = word[word.index(a) + 1:]
    else:
        print('I hate UCPC')
        break
if i == 4:
    print('I love UCPC')