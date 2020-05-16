
def servicelane(width, i , j):
    s = width[i]
    i += 1
    while i <= j:
        s = min(s, width[i])
        i += 1

    return s


n, t = map(int, input().split())
width = list(map(int, input().split()))
for case in range(t):
    i, j = map(int, input().split())
    print(servicelane(width, i, j))
