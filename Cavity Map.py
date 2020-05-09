
def cavitymap(arr, n):
    for i in range(1, n - 1, 1):
        for j in range(1, n - 1, 1):
            if arr[i][j] > arr[i-1][j] and arr[i][j] > arr[i][j-1] and arr[i][j] > arr[i+1][j] and arr[i][j] > arr[i][j+1]:
                arr[i][j] = "X"

    return 0
n = int(input())
arr = []
for i in range(n):
    a = list(input())
    arr.append(a)
cavitymap(arr, n)
for a in arr:
    print("".join(a))
