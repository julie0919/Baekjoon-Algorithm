num = 1000 - int(input())
count = 0
while True:
    if num >= 500:
        count += 1
        num = num - 500
    elif num >= 100:
        count += 1
        num = num - 100
    elif num >= 50:
        count += 1
        num = num - 50
    elif num >= 10:
        count += 1
        num = num - 10
    elif num >= 5:
        count += 1
        num = num - 5
    elif num >= 1:
        count += 1
        num = num - 1    
    
    if num == 0:
        break
print(count)