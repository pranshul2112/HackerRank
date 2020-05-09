
def manasa(n, a, b):
    s = set() # Stores data in unsorted form
    for i in range(n):
        s.add(i * a + (n - i - 1)* b)
    s = list(s)
    s.sort()
    return " ".join([str(x) for x in s])

t = int(input())
for t_tr in range(t):
    n = int(input())
    a = int(input())
    b = int(input())
    print(manasa(n, a, b))
