
def balancedSums(arr):
    check = arr[0]
    n = len(arr)
    s = sum(arr)
    if s - check == 0:
        return "YES"

    for i in range(1, n):
        if s - arr[i] - check == check or s - arr[i] == 0:
            return "YES"

        check += arr[i]

    return "NO"


T = int(input().strip())

for T_itr in range(T):
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    print(balancedSums(arr))

