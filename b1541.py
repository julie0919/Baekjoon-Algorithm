func = input().split('-')

result = 0
for i in func[0].split('+'):
    result += int(i)

for i in func[1:]:
    for j in i.split('+'):
        result -= int(j)

print(result)
        