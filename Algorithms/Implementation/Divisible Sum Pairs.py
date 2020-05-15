nk = input().split()
n = int(nk[0])
k = int(nk[1])
s = 0
a = list(map(int, input().rstrip().split()))
for i in range(n):
    for j in range(i, n):
        if i < j:
            if (a[i] + a[j]) % k == 0:
                s += 1
print(s)
