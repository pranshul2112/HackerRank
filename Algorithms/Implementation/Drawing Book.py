def abc(p):
    return 1 + (p//2)
def dbz(n,p):
    return min(abc(p) - abc(1), abc(n) - abc(p))
n = int(input())
p = int(input())
print(dbz(n,p))


