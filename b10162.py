t = int(input())

a = 300
b = 60
c = 10

acnt = 0
bcnt = 0
ccnt = 0

while True:
    if t - a >= 0:
        acnt += 1
        t = t - a
    elif t - b >= 0:
        bcnt += 1
        t = t - b
    elif t - c >= 0:
        ccnt += 1
        t = t - c
    elif t == 0:
        print(acnt, end=' ')
        print(bcnt, end=' ')
        print(ccnt,)
        break
    else:
        print(-1)
        break
