
def modFibo(a, b, n):
    for i in range(n-2):
        c = a + b*b
        a = b
        b = c
    return c

a, b, n = map(int, input().split())
print(modFibo(a, b, n))
