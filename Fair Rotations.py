def fairrotations(arr):
    n = len(arr)
    bread = 0
    if sum(arr) % 2 == 0:
        for i in range(n):
            if arr[i] % 2 == 1:
                    arr[i + 1] += 1
                    arr[i] += 1
                    bread += 2

        return bread
    else:
        return "NO"


n = int(input())
arr = list(map(int, input().split()))
print(fairrotations(arr))
