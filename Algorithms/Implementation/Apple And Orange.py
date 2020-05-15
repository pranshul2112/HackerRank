def countApplesAndOranges(s, t, a, b, apples, oranges):
    flagApple = 0
    flagOrange = 0
    for i in range (m):
        if apples[i] + a >= s and apples[i] + a <= t:
            flagApple += 1
    for i in range(n):
        if oranges[i] + b <= t and oranges[i] + b >= s:
            flagOrange += 1
    print(flagApple)
    print(flagOrange)


st = input().split()
s = int(st[0])
t = int(st[1])
ab = input().split()
a = int(ab[0])
b = int(ab[1])
mn = input().split()
m = int(mn[0])
n = int(mn[1])

apples = list(map(int, input().rstrip().split()))

oranges = list(map(int, input().rstrip().split()))

countApplesAndOranges(s, t, a, b, apples, oranges)
