
def parlor(arr, m):
    n = len(arr)
    for i in range(n):
        for j in range(i):
            if arr[i] + arr[j] == m:
                return " ".join(str(x) for x in (j +1, i + 1))

    return "No"


t = int(input())
for case in range(t):
    m = int(input())
    n = int(input())
    arr = list(map(int, input().split()))
    print(parlor(arr, m))
