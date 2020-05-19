
def insertionSort(arr):
    m = arr[-1]
    
    for i in range(n - 2, -1, -1):
        if arr[i] > m:
            arr[i + 1] = arr[i]
            print(*arr)

        else:
            arr[i + 1] = m
            print(*arr)
            return

    arr[0] = m
    print(*arr)
    return


n = int(input())
arr = list(map(int, input().split()))
insertionSort(arr)
