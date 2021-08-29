N = int(input())

def prime(strnum):
    if (strnum < 2):
        return False
    for i in range(2, int(strnum**0.5) + 1):
        if (strnum%i == 0):
            return False
    return True


def test(num):
    if len(str(num)) == N:
        print(num)
    else:
        for i in range(10):
            temp = num*10 + i
            if prime(temp):
                test(temp)

test(2)
test(3)
test(5)
test(7)
