#  https://www.hackerrank.com/challenges/flipping-the-matrix/problem

def flippin(n, arr):
    m = 2 * n
    s = 0
    for i in range(n):
        for j in range(n):
            s += max(arr[i][j], arr[m-1-i][j], arr[i][m-1-j], arr[m-1-i][m-1-j])

    return s

q = int(input())
for _ in range(q):
    n = int(input())
    arr = []
    for i in range(2 * n):
        a = list(map(int, input().split()))
        arr.append(a)
    print(flippin(n, arr))
