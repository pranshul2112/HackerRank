
def minimumSwaps(arr):
    swapCount = 0
    temp = [0] * len(arr)

    for index, value in enumerate(arr):
        temp[value - 1] = index

    for i in range(len(arr)):
        if arr[i] != i + 1:
            t = temp[i]
            arr[i], arr[t] = i + 1, arr[i]
            temp[i], temp[arr[t] - 1] = i, t
            swapCount += 1

    return swapCount

n = int(input())
arr = list(map(int, input().rstrip().split()))
res = minimumSwaps(arr)
print(res)
