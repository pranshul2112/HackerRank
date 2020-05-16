
def JumpingOnClouds(c, k, n):
    e = 100
    e -= 1
    i = (0 + k) % n
    if c[i] == 1:
        e -= 2
    while i != 0:
        e -= 1
        i = (i + k) % n
        if c[i] == 1:
            e -= 2
    return e


nk = input().split()
n = int(nk[0])
k = int(nk[1])
c = list(map(int, input().rstrip().split()))
print(JumpingOnClouds(c, k, n))
