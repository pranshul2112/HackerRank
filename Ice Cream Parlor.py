def parlor(arr, m):
    n = len(arr)
    for i in range(n):
        for j in range(i):
            if arr[i] + arr[j] == m:
                return " ".join(str(x) for x in (j +1, i + 1))

t = int(input())
for case in range(t):

    m = int(input())
    n = int(input())
    arr = [1, 4, 5, 3, 2]
    print(parlor(arr, m))
