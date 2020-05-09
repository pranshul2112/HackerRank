
n = int(input().strip())
a = list(map(int, input().rstrip().split()))
dm = input().rstrip().split()
d = int(dm[0])
m = int(dm[1])
flag = 0

for i in range(len(a)):
    count = k = 0
    while count < m:
        k += a[i + count]
        count += 1
    if k == d:
        flag += 1
    if (i + count == len(a)):
        break
print(flag)
