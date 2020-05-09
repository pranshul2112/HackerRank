
n = int(input().strip())
arr = list(map(int, input().strip().split()))
k = [0] * 100
flag = 0
for i in arr:
        k[i] += 1
for i in range(1, n):
        flag = max(flag, k[i] + k[i - 1])
print(flag)
