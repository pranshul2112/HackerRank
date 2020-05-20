from bisect import bisect_left, insort_left

n, d = map(int, input().split())
arr = list(map(int, input().split()))
flag = 0

temp = sorted(arr[:d])


def median():
    return temp[d // 2] if d % 2 == 1 else ((temp[d // 2] + temp[d // 2 - 1]) / 2)


for i in range(d, n):
    if arr[i] >= 2 * median():
        flag += 1
    del temp[bisect_left(temp, arr[i - d])]
    insort_left(temp, arr[i])
    
print(flag)
