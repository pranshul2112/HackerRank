
def strangeCounter(t):
    val = 3
    while t > val:
        t -= val
        val *= 2

    return val - t + 1

t = int(input())

print(strangeCounter(t))
