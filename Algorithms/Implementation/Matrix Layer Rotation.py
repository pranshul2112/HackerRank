
def matrixrotation(arr, m, n, r, q):
    x = []
    for i in range(q, m - q - 1):  x.append(arr[i][q])
        
    for i in range(q, n - q):  x.append(arr[m - q - 1][i])
    
    for i in range(m - q - 2, q, -1):  x.append(arr[i][n - q - 1])
    
    for i in range(n - q - 1, q, -1):  x.append(arr[q][i])

    cnst = len(x)
    r = cnst - (r % cnst)
    y = x[r:] + x[:r]
    count = 0

    for i in range(q, m - q - 1):
        arr[i][q] = y[count]
        count += 1

    for i in range(q, n - q):
        arr[m - q - 1][i] = y[count]
        count += 1

    for i in range(m - q - 2, q, -1):
        arr[i][n - q - 1] = y[count]
        count += 1

    for i in range(n - q - 1, q, -1):
        arr[q][i] = y[count]
        count += 1

    return


m, n, r = map(int, input().split())
arr = []
for i in range(m):
    a = list(map(int, input().split()))
    arr.append(a)
p = min(n, m) // 2
for q in range(p):
    matrixrotation(arr, m, n, r, q)

for i in range(m):
    print(" ".join(map(str, arr[i])))
    
