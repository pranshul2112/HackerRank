
n = int(input())
a = list(map(int, input().split()))
op = ['*'] * (n - 1)
possible = [[None] * 101 for i in range(n)]
possible[0][a[0]] = True
end = n - 1

for i in range(n - 1):
    if possible[i][0]:
        end = i
        break
    for x in range(101):
        if possible[i][x]:
            possible[i + 1][(x + a[i + 1]) % 101] = ('+', x)
            possible[i + 1][(x + 101 - a[i + 1]) % 101] = ('-', x)
            possible[i + 1][(x * a[i + 1]) % 101] = ('*', x)
                        
x = 0
for i in range(end, 0, -1):
    op[i - 1] = possible[i][x][0]
    x = possible[i][x][1]
print(''.join(str(x) for t in zip(a, op) for x in t) + str(a[-1]))
