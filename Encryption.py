import math


def encryption(s):
    l = len(s)
    row = round(math.sqrt(l))
    col = row if (row >= math.sqrt(l)) else row + 1
    for j in range(col):
        for i in range(j, l, col):
            print(s[i], end='')
        print(end=' ')


L = input()
encryption(L)
