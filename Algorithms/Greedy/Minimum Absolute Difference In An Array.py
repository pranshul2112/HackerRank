
def minimumAbsoluteDifference(arr):
    k = 2 ** 31
    arr.sort()
    for i in range(len(arr) - 1):
        k = min(k, abs(arr[i] - arr[i+1]))
    return k

n = int(input())

arr = list(map(int, input().rstrip().split()))

print(minimumAbsoluteDifference(arr))
